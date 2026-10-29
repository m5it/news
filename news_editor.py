#!/usr/bin/env python3
"""
news_editor.py — PyQt5 lightweight editor for news repo
- Left: TreeView (categories + entries + detail files) — all dirs are tags
- Right: Top = AI chat (left history / right input), Bottom = Preview + Edit Form
- Ollama local support with multiple servers (192.168.1.1, 192.168.0.1, localhost)
- Lightweight: no heavy deps, QThread for Ollama, lazy file loading
"""
import sys
import os
import json
import re
import requests
from pathlib import Path
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QSplitter, QTreeView, QListWidget, QListWidgetItem,
    QVBoxLayout, QHBoxLayout, QFormLayout, QTextEdit, QTextBrowser, QLineEdit, QLabel,
    QPushButton, QComboBox, QDateEdit, QMessageBox, QInputDialog, QMenu, QAction,
    QStatusBar, QToolBar, QGroupBox, QTabWidget, QFileDialog, QDialog, QDialogButtonBox,
    QPlainTextEdit
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QDate, QModelIndex, QSize
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont

# local
import news_parser

APP_NAME = "gitnewsadmin"
# Config in ~/.config/gitnewsadmin/config.json (XDG), fallback to ./editor_config.json for portable use
def _config_paths():
    xdg = Path.home() / ".config" / APP_NAME / "config.json"
    local = Path("editor_config.json")
    return xdg, local

CONFIG_PATH, LOCAL_CONFIG_PATH = _config_paths()
DEFAULT_CONFIG = {
    "ollama_servers": [
        {"name": "local", "url": "http://localhost:11434"},
        {"name": "main-69", "url": "http://192.168.0.69:11434"},
        {"name": "lan-1", "url": "http://192.168.1.1:11434"},
        {"name": "lan-2", "url": "http://192.168.0.1:11434"},
    ],
    "active_server": "http://192.168.0.69:11434",
    "model": "qwen2.5:7b",
    "theme": "light",
    "window": {"x": None, "y": None, "width": 1400, "height": 850, "maximized": False,
               "splitter_main": None, "splitter_right": None, "splitter_ai": None, "splitter_bottom": None}
}

def load_config():
    # prefer XDG, migrate from local if needed
    xdg, local = _config_paths()
    src = None
    if xdg.exists():
        src = xdg
    elif local.exists():
        # migrate local -> xdg
        try:
            data = json.loads(local.read_text(encoding="utf-8"))
            xdg.parent.mkdir(parents=True, exist_ok=True)
            xdg.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            src = xdg
        except:
            src = local
    if src and src.exists():
        try:
            data = json.loads(src.read_text(encoding="utf-8"))
            cfg = {**DEFAULT_CONFIG, **data}
            if "ollama_servers" not in cfg:
                cfg["ollama_servers"] = DEFAULT_CONFIG["ollama_servers"]
            if "window" not in cfg:
                cfg["window"] = DEFAULT_CONFIG["window"]
            else:
                # merge window defaults
                cfg["window"] = {**DEFAULT_CONFIG["window"], **cfg["window"]}
            return cfg
        except:
            return DEFAULT_CONFIG.copy()
    return DEFAULT_CONFIG.copy()

def save_config(cfg):
    xdg, local = _config_paths()
    # always save to XDG
    xdg.parent.mkdir(parents=True, exist_ok=True)
    xdg.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    # also keep local copy for portability (optional)
    try:
        local.write_text(json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8")
    except:
        pass


# --- Ollama thread (non-blocking, keeps UI light for weak PCs) ---
class OllamaWorker(QThread):
    chunk = pyqtSignal(str)
    finished_ok = pyqtSignal()
    error = pyqtSignal(str)

    def __init__(self, server_url, model, prompt, context=""):
        super().__init__()
        self.server_url = server_url.rstrip("/")
        self.model = model
        self.prompt = prompt
        self.context = context

    def run(self):
        try:
            url = f"{self.server_url}/api/chat"
            # Build messages: context + prompt
            messages = []
            if self.context:
                messages.append({"role": "system", "content": f"You are editor assistant for news project. Context file:\n{self.context[:8000]}"})
            messages.append({"role": "user", "content": self.prompt})
            payload = {"model": self.model, "messages": messages, "stream": True}
            r = requests.post(url, json=payload, stream=True, timeout=60)
            r.raise_for_status()
            for line in r.iter_lines():
                if not line:
                    continue
                try:
                    obj = json.loads(line.decode("utf-8"))
                    if "message" in obj and "content" in obj["message"]:
                        self.chunk.emit(obj["message"]["content"])
                    if obj.get("done"):
                        break
                except:
                    continue
            self.finished_ok.emit()
        except Exception as e:
            self.error.emit(str(e))


class OllamaModelsWorker(QThread):
    result = pyqtSignal(list)
    error = pyqtSignal(str)
    def __init__(self, server_url):
        super().__init__()
        self.server_url = server_url.rstrip("/")
    def run(self):
        try:
            r = requests.get(f"{self.server_url}/api/tags", timeout=5)
            r.raise_for_status()
            data = r.json()
            models = [m["name"] for m in data.get("models", [])]
            self.result.emit(models)
        except Exception as e:
            self.error.emit(str(e))


# --- Server dialog ---
class ServerDialog(QDialog):
    def __init__(self, cfg, parent=None):
        super().__init__(parent)
        self.cfg = cfg
        self.setWindowTitle("Ollama Servers")
        self.resize(500, 300)
        lay = QVBoxLayout(self)
        self.list = QListWidget()
        self.refresh_list()
        lay.addWidget(self.list)
        btns = QHBoxLayout()
        for txt, fn in [("Add", self.add_srv), ("Remove", self.remove_srv), ("Edit", self.edit_srv)]:
            b = QPushButton(txt); b.clicked.connect(fn); btns.addWidget(b)
        lay.addLayout(btns)
        bb = QDialogButtonBox(QDialogButtonBox.Close)
        bb.rejected.connect(self.reject)
        lay.addWidget(bb)

    def refresh_list(self):
        self.list.clear()
        for s in self.cfg["ollama_servers"]:
            marker = " ● active" if s["url"] == self.cfg["active_server"] else ""
            self.list.addItem(f'{s["name"]} — {s["url"]}{marker}')

    def add_srv(self):
        name, ok = QInputDialog.getText(self, "Add server", "Name:")
        if not ok or not name: return
        url, ok = QInputDialog.getText(self, "Add server", "URL (http://ip:11434):")
        if not ok or not url: return
        self.cfg["ollama_servers"].append({"name": name, "url": url.strip()})
        save_config(self.cfg); self.refresh_list()

    def remove_srv(self):
        row = self.list.currentRow()
        if row < 0: return
        del self.cfg["ollama_servers"][row]
        if not self.cfg["ollama_servers"]:
            self.cfg["ollama_servers"] = DEFAULT_CONFIG["ollama_servers"]
        save_config(self.cfg); self.refresh_list()

    def edit_srv(self):
        row = self.list.currentRow()
        if row < 0: return
        s = self.cfg["ollama_servers"][row]
        url, ok = QInputDialog.getText(self, "Edit URL", "URL:", text=s["url"])
        if ok and url:
            s["url"] = url.strip()
            save_config(self.cfg); self.refresh_list()


class ArchiveDialog(QDialog):
    """Archive: selected / previous month / by month / older than date — tags preserved"""
    def __init__(self, current_path: Path, entries, parent=None):
        super().__init__(parent)
        self.current_path = current_path
        self.entries = entries  # list[NewsEntry]
        self.setWindowTitle(f"Archive — {current_path.name}")
        self.resize(560, 420)
        lay = QVBoxLayout(self)

        # Info
        lay.addWidget(QLabel(f"<b>Source:</b> {current_path} — {len(entries)} entries"))
        # detect months present
        months = {}
        for e in entries:
            dt = news_parser.parse_date(e.date_str)
            if dt:
                k = f"{dt.year}-{dt.strftime('%m')} ({dt.strftime('%B %Y')})"
                months[k] = months.get(k, 0) + 1
        month_info = ", ".join([f"{k}: {v}" for k, v in sorted(months.items())])
        lay.addWidget(QLabel(f"Months in file: {month_info or 'unknown dates'}"))
        lay.addWidget(QLabel("Tags are always preserved — archived entry keeps its > tags, emoji, Key insight, links."))

        # Mode
        self.mode_combo = QComboBox()
        self.mode_combo.addItems([
            "Selected entries (from tree, multi-select)",
            "Previous month (auto)",
            "By month (choose month)",
            "Older than date (keep recent, archive older)",
            "Keep last N entries, archive rest"
        ])
        lay.addWidget(QLabel("What to archive:"))
        lay.addWidget(self.mode_combo)

        # Params row
        param_box = QGroupBox("Parameters")
        param_lay = QFormLayout(param_box)
        self.month_combo = QComboBox()
        for k in sorted(months.keys()):
            self.month_combo.addItem(k, k.split()[0])
        self.date_edit = QDateEdit(QDate.currentDate().addMonths(-1))
        self.date_edit.setCalendarPopup(True); self.date_edit.setDisplayFormat("yyyy-MM-dd")
        self.keep_spin = QComboBox(); [self.keep_spin.addItem(str(n)) for n in [20,30,50,100,150]]
        self.keep_spin.setCurrentText("50")
        self.archive_target = QLineEdit()
        self.archive_target.setPlaceholderText("auto → README_YYYY_MM.md (based on moved entries) or pick existing")
        # file picker
        pick_btn = QPushButton("Browse")
        target_row = QHBoxLayout(); target_row.addWidget(self.archive_target, stretch=1); target_row.addWidget(pick_btn)
        target_w = QWidget(); target_w.setLayout(target_row)
        param_lay.addRow("Month:", self.month_combo)
        param_lay.addRow("Cutoff date:", self.date_edit)
        param_lay.addRow("Keep recent N:", self.keep_spin)
        param_lay.addRow("Target archive file:", target_w)
        lay.addWidget(param_box)

        def pick():
            fn, _ = QFileDialog.getSaveFileName(self, "Archive target", str(Path(".").resolve()), "Markdown (*.md)")
            if fn: self.archive_target.setText(fn)
        pick_btn.clicked.connect(pick)

        # Preview
        self.preview_label = QLabel()
        self.preview_label.setWordWrap(True)
        self.preview_label.setStyleSheet("color:#555; background:#f5f5f5; padding:6px;")
        lay.addWidget(self.preview_label)

        def update_preview():
            mode = self.mode_combo.currentIndex()
            preview = ""
            if mode == 1:  # previous month
                from datetime import datetime as dt
                cur = datetime.now()
                prev_m = cur.month - 1 if cur.month > 1 else 12
                prev_y = cur.year if cur.month > 1 else cur.year - 1
                preview = f"Will archive all entries from {prev_y}-{prev_m:02d} (previous month) → {'auto' if not self.archive_target.text() else self.archive_target.text()}. Tags kept."
            elif mode == 2:
                mk = self.month_combo.currentData() or ""
                preview = f"Will archive all entries from month {mk}. Tags kept."
            elif mode == 3:
                preview = f"Will archive entries older than {self.date_edit.date().toString('yyyy-MM-dd')}, keep newer. Tags kept."
            elif mode == 4:
                preview = f"Will keep newest {self.keep_spin.currentText()} entries in {self.current_path.name}, archive rest. Tags kept."
            else:
                preview = "Will archive entries you selected in tree (Ctrl+click multi-select). Tags kept."
            self.preview_label.setText(preview)
        self.mode_combo.currentIndexChanged.connect(update_preview)
        self.month_combo.currentIndexChanged.connect(update_preview)
        self.date_edit.dateChanged.connect(update_preview)
        self.keep_spin.currentIndexChanged.connect(update_preview)
        update_preview()

        bb = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        bb.accepted.connect(self.accept); bb.rejected.connect(self.reject)
        lay.addWidget(bb)

    def get_params(self):
        mode = self.mode_combo.currentIndex()
        target = Path(self.archive_target.text().strip()) if self.archive_target.text().strip() else None
        return {"mode": mode, "month_key": self.month_combo.currentData(), "cutoff": self.date_edit.date().toPyDate(), "keep_n": int(self.keep_spin.currentText()), "target": target}


# --- Main Window ---
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.cfg = load_config()
        self.root = Path(".").resolve()
        self.current_path: Path | None = None
        self.current_entry: news_parser.NewsEntry | None = None
        self.current_entry_index: int | None = None
        self.current_detail_path: Path | None = None
        self.ollama_worker = None

        self.setWindowTitle("News Editor — PyQt5 + Ollama (lightweight)")
        # Restore window geometry from ~/.config/gitnewsadmin/config.json
        wcfg = self.cfg.get("window", {})
        if wcfg.get("width") and wcfg.get("height"):
            self.resize(wcfg["width"], wcfg["height"])
        else:
            self.resize(1400, 850)
        if wcfg.get("x") is not None and wcfg.get("y") is not None:
            self.move(wcfg["x"], wcfg["y"])
        if wcfg.get("maximized"):
            self.showMaximized()

        # Toolbar: servers + model
        tb = QToolBar("Ollama")
        tb.setMovable(False)
        self.addToolBar(tb)
        tb.addWidget(QLabel("  Server: "))
        self.server_combo = QComboBox()
        self.server_combo.setMinimumWidth(220)
        self.refresh_server_combo()
        self.server_combo.currentIndexChanged.connect(self.on_server_changed)
        tb.addWidget(self.server_combo)
        tb.addWidget(QLabel("  Model: "))
        self.model_combo = QComboBox()
        self.model_combo.setEditable(True)
        self.model_combo.setMinimumWidth(200)
        self.model_combo.addItem(self.cfg.get("model", ""))
        self.model_combo.currentTextChanged.connect(self.on_model_changed)
        tb.addWidget(self.model_combo)
        btn_test = QPushButton("Test")
        btn_test.clicked.connect(self.test_connection)
        tb.addWidget(btn_test)
        btn_refresh = QPushButton("Refresh models")
        btn_refresh.clicked.connect(self.refresh_models)
        tb.addWidget(btn_refresh)
        btn_servers = QPushButton("Manage servers")
        btn_servers.clicked.connect(self.manage_servers)
        tb.addWidget(btn_servers)

        # Central splitter: left tree, right editor+ai
        central = QSplitter(Qt.Horizontal)
        self.setCentralWidget(central)

        # LEFT: tree + actions
        left_w = QWidget()
        left_lay = QVBoxLayout(left_w)
        left_lay.setContentsMargins(4,4,4,4)
        left_w.setMinimumWidth(320)

        left_lay.addWidget(QLabel("<b>Categories / Files</b> (all dirs are tags)"))
        self.tree_model = QStandardItemModel()
        self.tree_model.setHorizontalHeaderLabels(["News"])
        self.tree = QTreeView()
        self.tree.setModel(self.tree_model)
        self.tree.setHeaderHidden(True)
        self.tree.setSelectionMode(QTreeView.ExtendedSelection)
        self.tree.setSelectionBehavior(QTreeView.SelectRows)
        self.tree.setUniformRowHeights(True)
        self.tree.clicked.connect(self.on_tree_clicked)
        self.tree.setContextMenuPolicy(Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_tree_context)
        left_lay.addWidget(self.tree, stretch=1)

        # left actions
        left_btns = QHBoxLayout()
        for txt, fn in [("New File", self.new_file), ("New Category", self.new_category), ("Delete", self.delete_selected), ("Fix Separators", self.fix_separators)]:
            b = QPushButton(txt); b.clicked.connect(fn); left_btns.addWidget(b)
        left_lay.addLayout(left_btns)
        arch_row = QHBoxLayout()
        self.btn_archive = QPushButton("📦 Archive…")
        self.btn_archive.setStyleSheet("background:#FF9800; color:white; font-weight:bold; padding:4px;")
        self.btn_archive.clicked.connect(self.archive_dialog)
        self.btn_archive.setToolTip("Archive old/selected entries to README_YYYY_MM.md — tags preserved")
        arch_row.addWidget(self.btn_archive, stretch=1)
        left_lay.addLayout(arch_row)
        self.status_label = QLabel("Ready — local Ollama, weak-PC friendly (lazy load)")
        left_lay.addWidget(self.status_label)

        central.addWidget(left_w)

        # RIGHT: vertical splitter: AI top + Edit+Preview bottom
        right_split = QSplitter(Qt.Vertical)
        central.addWidget(right_split)

        # RIGHT TOP: AI panel (h-split: history left, input right)
        ai_group = QGroupBox("AI — Ollama (local)")
        ai_lay = QVBoxLayout(ai_group)
        ai_split = QSplitter(Qt.Horizontal)

        # AI history
        hist_w = QWidget()
        hist_lay = QVBoxLayout(hist_w)
        hist_lay.setContentsMargins(2,2,2,2)
        hist_lay.addWidget(QLabel("AI responses / requests"))
        self.ai_history = QTextBrowser()
        self.ai_history.setPlaceholderText("AI answers appear here. Ask to polish, translate, suggest tags, make Key Insight...")
        self.ai_history.setOpenExternalLinks(False)
        hist_lay.addWidget(self.ai_history, stretch=1)
        btn_row = QHBoxLayout()
        self.btn_apply_ai = QPushButton("Apply last AI → Title/Body")
        self.btn_apply_ai.clicked.connect(self.apply_ai_to_fields)
        self.btn_clear_ai = QPushButton("Clear")
        self.btn_clear_ai.clicked.connect(lambda: self.ai_history.clear())
        btn_row.addWidget(self.btn_apply_ai); btn_row.addWidget(self.btn_clear_ai)
        hist_lay.addLayout(btn_row)
        ai_split.addWidget(hist_w)

        # AI input
        input_w = QWidget()
        input_lay = QVBoxLayout(input_w)
        input_lay.setContentsMargins(2,2,2,2)
        input_lay.addWidget(QLabel("Your prompt (context = selected file auto-included)"))
        self.ai_input = QTextEdit()
        self.ai_input.setPlaceholderText("e.g. Polish this entry, keep my voice. Suggest emoji and tags. Make Key insight...")
        self.ai_input.setMinimumHeight(80)
        input_lay.addWidget(self.ai_input, stretch=1)
        qbtns = QHBoxLayout()
        for label, prompt in [
            ("Polish", "Polish the selected news entry for clarity and grammar, keep my voice and opinion."),
            ("Tags", "Suggest tags/categories for this entry as comma list."),
            ("Insight", "Write a **Key insight:** 1-2 sentences for this entry."),
            ("Translate EN", "Translate this entry to English, keep tone."),
            ("Fix MD", "Fix markdown formatting, ensure header is ## Date — Title and separators are ---."),
        ]:
            b = QPushButton(label); b.clicked.connect(lambda _, p=prompt: self.send_ai(p)); qbtns.addWidget(b)
        input_lay.addLayout(qbtns)
        send_row = QHBoxLayout()
        self.btn_send = QPushButton("Send to Ollama ▶")
        self.btn_send.setStyleSheet("font-weight:bold; background:#4CAF50; color:white; padding:6px;")
        self.btn_send.clicked.connect(lambda: self.send_ai(None))
        send_row.addWidget(self.btn_send, stretch=1)
        input_lay.addLayout(send_row)
        ai_split.addWidget(input_w)

        ai_split.setSizes([600, 400])
        ai_lay.addWidget(ai_split, stretch=1)
        right_split.addWidget(ai_group)

        # RIGHT BOTTOM: Edit form + Preview
        bottom = QSplitter(Qt.Horizontal)
        # Form
        form_w = QWidget()
        form_lay = QVBoxLayout(form_w)
        form_lay.addWidget(QLabel("<b>Editor</b> — select tree item → edit here. Bottom is preview."))
        # fields
        grid = QFormLayout()
        self.ed_date = QLineEdit(); self.ed_date.setPlaceholderText("October 29, 2026")
        self.ed_title = QLineEdit(); self.ed_title.setPlaceholderText("Title")
        self.ed_emoji = QLineEdit(); self.ed_emoji.setPlaceholderText("📰"); self.ed_emoji.setMaximumWidth(80)
        self.ed_tags = QLineEdit(); self.ed_tags.setPlaceholderText("Tag1 | Tag2 | Tag3 (shown as > ...)")
        self.ed_link = QLineEdit(); self.ed_link.setPlaceholderText("TECH/file.md or leave empty (auto creates link if detail file)")
        date_row = QHBoxLayout()
        date_row.addWidget(self.ed_date, stretch=1); date_row.addWidget(QLabel("Emoji:")); date_row.addWidget(self.ed_emoji)
        date_w = QWidget(); date_w.setLayout(date_row)
        grid.addRow("Date:", date_w)
        grid.addRow("Title:", self.ed_title)
        grid.addRow("Tags (>):", self.ed_tags)
        grid.addRow("Detail link:", self.ed_link)
        form_lay.addLayout(grid)
        form_lay.addWidget(QLabel("Body (markdown, bullets with -):"))
        self.ed_body = QPlainTextEdit()
        self.ed_body.setPlaceholderText("- Your news text here...\n- Second bullet")
        self.ed_body.textChanged.connect(self.update_preview)
        form_lay.addWidget(self.ed_body, stretch=1)
        form_lay.addWidget(QLabel("Key insight:"))
        self.ed_insight = QLineEdit()
        self.ed_insight.setPlaceholderText("One sentence takeaway...")
        self.ed_insight.textChanged.connect(self.update_preview)
        form_lay.addWidget(self.ed_insight)
        # form buttons
        fbtns = QHBoxLayout()
        self.btn_save = QPushButton("💾 Save"); self.btn_save.clicked.connect(self.save_current)
        self.btn_new_entry = QPushButton("＋ New Entry"); self.btn_new_entry.clicked.connect(self.new_entry_in_current)
        self.btn_delete_entry = QPushButton("🗑 Remove Entry"); self.btn_delete_entry.clicked.connect(self.delete_entry)
        self.btn_preview_raw = QPushButton("↻ Preview"); self.btn_preview_raw.clicked.connect(self.update_preview)
        for b in [self.btn_save, self.btn_new_entry, self.btn_delete_entry, self.btn_preview_raw]:
            fbtns.addWidget(b)
        form_lay.addLayout(fbtns)
        # connect title/date changes to preview
        for w in [self.ed_date, self.ed_title, self.ed_tags, self.ed_link, self.ed_emoji]:
            w.textChanged.connect(self.update_preview)

        bottom.addWidget(form_w)

        # Preview
        preview_w = QWidget()
        preview_lay = QVBoxLayout(preview_w)
        preview_lay.addWidget(QLabel("<b>Preview</b> (what will be written to README)"))
        self.preview = QTextBrowser()
        self.preview.setOpenExternalLinks(True)
        self.preview.setStyleSheet("background:#fafafa;")
        preview_lay.addWidget(self.preview, stretch=1)
        bottom.addWidget(preview_w)
        bottom.setSizes([600, 500])

        right_split.addWidget(bottom)
        right_split.setSizes([320, 500])

        # status bar
        self.setStatusBar(QStatusBar())

        # Restore splitters from config
        wcfg = self.cfg.get("window", {})
        # Need to apply after show, store for later
        self._pending_splitters = {
            "main": wcfg.get("splitter_main"),
            "right": wcfg.get("splitter_right"),
            "ai": wcfg.get("splitter_ai"),
            "bottom": wcfg.get("splitter_bottom"),
        }

        # load tree
        self.rebuild_tree()
        self.refresh_models()
        # keep last AI text for Apply
        self.last_ai_text = ""

        # Keep refs for saving
        self._central_splitter = central
        self._right_splitter = right_split
        self._ai_splitter = ai_split
        self._bottom_splitter = bottom

    def showEvent(self, event):
        super().showEvent(event)
        # Apply splitter sizes once widgets are laid out
        if hasattr(self, '_pending_splitters') and self._pending_splitters:
            p = self._pending_splitters
            if p.get("main"):
                try: self._central_splitter.setSizes(p["main"])
                except: pass
            if p.get("right"):
                try: self._right_splitter.setSizes(p["right"])
                except: pass
            if p.get("ai"):
                try: self._ai_splitter.setSizes(p["ai"])
                except: pass
            if p.get("bottom"):
                try: self._bottom_splitter.setSizes(p["bottom"])
                except: pass
            self._pending_splitters = None

    def closeEvent(self, event):
        # Save window geometry + splitter sizes to ~/.config/gitnewsadmin/config.json
        try:
            cfg = load_config()
            w = cfg.get("window", {}).copy()
            w["width"] = self.width()
            w["height"] = self.height()
            w["x"] = self.x()
            w["y"] = self.y()
            w["maximized"] = self.isMaximized()
            w["splitter_main"] = self._central_splitter.sizes() if hasattr(self, '_central_splitter') else None
            w["splitter_right"] = self._right_splitter.sizes() if hasattr(self, '_right_splitter') else None
            w["splitter_ai"] = self._ai_splitter.sizes() if hasattr(self, '_ai_splitter') else None
            w["splitter_bottom"] = self._bottom_splitter.sizes() if hasattr(self, '_bottom_splitter') else None
            cfg["window"] = w
            # preserve ollama/model choices if changed
            cfg["active_server"] = self.cfg.get("active_server", cfg.get("active_server"))
            cfg["model"] = self.model_combo.currentText().strip() if hasattr(self, 'model_combo') else cfg.get("model")
            cfg["ollama_servers"] = self.cfg.get("ollama_servers", cfg.get("ollama_servers"))
            save_config(cfg)
        except Exception as e:
            print(f"save window state failed: {e}")
        super().closeEvent(event)

    # --- Tree ---
    def rebuild_tree(self):
        self.tree_model.clear()
        self.tree_model.setHorizontalHeaderLabels(["News"])
        root = Path(".").resolve()
        data = news_parser.parse_all(root)
        # order: readme files first, then dirs, then root
        order = ["readme", "readme_tech", "readme_sport", "readme_archive", "readme_2026_07", "readme_2", "tech", "sport", "default", "private", "_root"]
        for key in order + [k for k in data.keys() if k not in order]:
            if key not in data:
                continue
            v = data[key]
            info = v["info"]
            if "entries" in v:
                parent = QStandardItem(f"{info['path'].name}  ({len(v['entries'])} entries)")
                parent.setData({"kind": "readme", "path": str(info["path"]), "entries": v["entries"]}, Qt.UserRole)
                parent.setEditable(False)
                # add entries as children (lazy: show first 80, but all for now — still light)
                for idx, e in enumerate(v["entries"]):
                    label = f"{e.emoji + ' ' if e.emoji else ''}{e.date_str} — {e.title[:60]}"
                    child = QStandardItem(label)
                    child.setData({"kind": "entry", "path": str(info["path"]), "index": idx, "entry": e}, Qt.UserRole)
                    child.setEditable(False)
                    parent.appendRow(child)
                self.tree_model.appendRow(parent)
            elif "files" in v:
                label = f"{info['path'].name}/  ({len(v['files'])} files)"
                if key == "_root":
                    label = f"./  (root loose: {len(v['files'])} files)"
                parent = QStandardItem(label)
                parent.setData({"kind": "dir", "path": str(info["path"])}, Qt.UserRole)
                parent.setEditable(False)
                for f in v["files"]:
                    p = f["path"]
                    child = QStandardItem(p.name)
                    child.setData({"kind": "detail", "path": str(p)}, Qt.UserRole)
                    child.setEditable(False)
                    parent.appendRow(child)
                self.tree_model.appendRow(parent)
        self.tree.expandAll()
        self.tree.resizeColumnToContents(0)

    def on_tree_clicked(self, idx: QModelIndex):
        item = self.tree_model.itemFromIndex(idx)
        data = item.data(Qt.UserRole)
        if not data:
            return
        kind = data["kind"]
        if kind == "readme":
            # select file itself → show its header info, clear form
            self.current_path = Path(data["path"])
            self.current_entry = None
            self.current_detail_path = None
            self.ed_date.setText("")
            self.ed_title.setText(f"Editing {self.current_path.name} — add new entry with ＋ New Entry")
            self.ed_body.setPlainText("")
            self.ed_tags.setText(""); self.ed_insight.setText(""); self.ed_link.setText(""); self.ed_emoji.setText("")
            self.statusBar().showMessage(f"Selected {data['path']} — {len(data['entries'])} entries")
            self.update_preview()
        elif kind == "entry":
            self.current_path = Path(data["path"])
            self.current_entry_index = data["index"]
            self.current_entry = data["entry"]
            self.current_detail_path = None
            # fill form
            self.ed_date.setText(self.current_entry.date_str)
            self.ed_title.setText(self.current_entry.title)
            self.ed_emoji.setText(self.current_entry.emoji)
            self.ed_tags.setText(self.current_entry.tags)
            self.ed_body.setPlainText(self.current_entry.body)
            self.ed_insight.setText(self.current_entry.key_insight)
            # link: first TECH/SPORT-like href
            link = ""
            for txt, href in self.current_entry.links:
                if "/" in href and href.endswith(".md"):
                    link = href; break
            self.ed_link.setText(link)
            self.statusBar().showMessage(f"Editing entry {self.current_entry.date_str} — {self.current_entry.title[:40]}")
            self.update_preview()
        elif kind in ("dir", "detail"):
            p = Path(data["path"])
            if p.is_dir():
                self.current_path = p
                self.current_detail_path = None
                self.statusBar().showMessage(f"Category {p.name}/ — create New File inside")
                return
            # detail file
            self.current_detail_path = p
            self.current_path = p
            self.current_entry = None
            try:
                txt = p.read_text(encoding="utf-8")
            except Exception as e:
                txt = f"Error reading: {e}"
            self.ed_date.setText(p.stem.replace("_", " "))
            self.ed_title.setText(p.stem)
            self.ed_emoji.setText("")
            self.ed_tags.setText("")
            self.ed_body.setPlainText(txt)
            self.ed_insight.setText("")
            self.ed_link.setText("")
            self.statusBar().showMessage(f"Editing detail file {p}")
            self.update_preview(detail_mode=True)

    def on_tree_context(self, pos):
        idx = self.tree.indexAt(pos)
        if not idx.isValid():
            return
        item = self.tree_model.itemFromIndex(idx)
        data = item.data(Qt.UserRole)
        menu = QMenu(self)
        if data["kind"] in ("dir", "readme"):
            a = menu.addAction("New file here"); a.triggered.connect(self.new_file)
            a2 = menu.addAction("Rename"); a2.triggered.connect(lambda: self.rename_selected(item, data))
        if data["kind"] == "detail":
            a = menu.addAction("Delete file"); a.triggered.connect(self.delete_selected)
            b = menu.addAction("Rename file"); b.triggered.connect(lambda: self.rename_selected(item, data))
        menu.exec_(self.tree.viewport().mapToGlobal(pos))

    # --- Editor actions ---
    def new_category(self):
        name, ok = QInputDialog.getText(self, "New Category", "Directory name (e.g. MEMO):")
        if not ok or not name: return
        name = name.strip().replace(" ", "_").upper()
        p = Path(name)
        if p.exists():
            QMessageBox.warning(self, "Exists", f"{p} already exists"); return
        p.mkdir(parents=True, exist_ok=True)
        (p / ".gitkeep").write_text("", encoding="utf-8")
        self.rebuild_tree()

    def new_file(self):
        # determine target dir: selected dir or dir of selected file or DEFAULT
        target = Path(".")
        idx = self.tree.currentIndex()
        if idx.isValid():
            item = self.tree_model.itemFromIndex(idx)
            d = item.data(Qt.UserRole)
            if d["kind"] == "dir":
                target = Path(d["path"])
            elif d["kind"] == "detail":
                target = Path(d["path"]).parent
            elif d["kind"] == "readme":
                # choose TECH as default for readme context
                target = Path("TECH")
                if not target.exists():
                    target = Path(".")
        else:
            target = Path("TECH") if Path("TECH").exists() else Path(".")

        name, ok = QInputDialog.getText(self, "New file", f"Filename in {target} (without .md):")
        if not ok or not name: return
        fname = name.strip().replace(" ", "_").lower()
        if not fname.endswith(".md"):
            fname += ".md"
        p = target / fname
        if p.exists():
            QMessageBox.warning(self, "Exists", f"{p} exists"); return
        p.write_text(f"# {name}\n\nWrite your article here.\n", encoding="utf-8")
        self.rebuild_tree()

    def delete_selected(self):
        idx = self.tree.currentIndex()
        if not idx.isValid(): return
        item = self.tree_model.itemFromIndex(idx)
        data = item.data(Qt.UserRole)
        if data["kind"] == "detail":
            p = Path(data["path"])
            if QMessageBox.question(self, "Delete", f"Delete {p}?") != QMessageBox.Yes: return
            p.unlink(missing_ok=True)
            self.rebuild_tree()
        elif data["kind"] == "dir":
            p = Path(data["path"])
            if QMessageBox.question(self, "Delete category", f"Delete empty dir {p}? (files will remain if not empty)") != QMessageBox.Yes:
                return
            try:
                p.rmdir()
            except Exception as e:
                QMessageBox.warning(self, "Error", str(e))
            self.rebuild_tree()
        else:
            QMessageBox.information(self, "Info", "Select a detail file or empty category to delete. For README entries use Remove Entry.")

    def rename_selected(self, item, data):
        if data["kind"] == "detail":
            old = Path(data["path"])
            new, ok = QInputDialog.getText(self, "Rename", "New filename:", text=old.name)
            if not ok or not new: return
            newp = old.parent / new
            old.rename(newp)
            self.rebuild_tree()
        elif data["kind"] in ("dir", "readme"):
            QMessageBox.information(self, "Info", "Rename via filesystem for README/categories.")

    def new_entry_in_current(self):
        # Determine target README
        target = self.current_path
        if target is None or target.is_dir():
            # default to README.md
            target = Path("README.md")
            if not target.exists():
                target = Path("README_TECH.md")
        if target.is_dir():
            # inside a detail dir, create new detail file instead
            self.new_file(); return
        if target.suffix != ".md":
            target = Path("README.md")
        # Insert new entry form with today date
        today = datetime.now().strftime("%B %d, %Y")
        self.ed_date.setText(today)
        self.ed_title.setText("New title")
        self.ed_emoji.setText("📰")
        self.ed_tags.setText("")
        self.ed_body.setPlainText("- Write here...\n")
        self.ed_insight.setText("")
        self.ed_link.setText("")
        self.current_entry = None
        self.current_entry_index = None
        self.current_detail_path = None
        self.current_path = target
        self.statusBar().showMessage(f"New entry — will be appended to {target.name} on Save")
        self.update_preview()

    def delete_entry(self):
        if self.current_entry is None or self.current_path is None:
            QMessageBox.warning(self, "No entry", "Select an entry from tree first"); return
        if QMessageBox.question(self, "Delete entry", f"Remove '{self.current_entry.title}' from {self.current_path.name}?") != QMessageBox.Yes:
            return
        content = self.current_path.read_text(encoding="utf-8")
        entries = news_parser.parse_entries(content, source_file=str(self.current_path))
        # remove by index
        if self.current_entry_index is not None and 0 <= self.current_entry_index < len(entries):
            del entries[self.current_entry_index]
            # rebuild file: keep header (everything before first entry) + entries + footer
            self._write_entries_back(self.current_path, entries, content)
            self.rebuild_tree()
            self.statusBar().showMessage(f"Deleted entry from {self.current_path.name}")

    def fix_separators(self):
        for fn in Path(".").glob("README*.md"):
            content = fn.read_text(encoding="utf-8")
            fixed = news_parser.normalize_file_content(content)
            if fixed != content:
                fn.write_text(fixed, encoding="utf-8")
        QMessageBox.information(self, "Fixed", "Separators and headers normalized (-- → ---, # → ##) in README*.md")
        self.rebuild_tree()

    def archive_dialog(self):
        # Determine source file: current readme or README.md
        src = self.current_path
        if src is None or src.is_dir() or src.suffix != ".md":
            src = Path("README.md")
        if not src.exists():
            QMessageBox.warning(self, "No source", f"{src} not found"); return
        content = src.read_text(encoding="utf-8")
        entries = news_parser.parse_entries(content, str(src))
        if not entries:
            QMessageBox.information(self, "Archive", f"No entries to archive in {src.name}"); return
        dlg = ArchiveDialog(src, entries, self)
        if dlg.exec_() != QDialog.Accepted:
            return
        params = dlg.get_params()
        # Resolve entries to move based on mode
        to_move = []
        mode = params["mode"]
        target = params["target"]
        if mode == 0:
            # Selected entries from tree (multi-select)
            idxs = self.tree.selectionModel().selectedIndexes()
            sel_keys = set()
            for idx in idxs:
                item = self.tree_model.itemFromIndex(idx)
                if not item: continue
                d = item.data(Qt.UserRole)
                if d and d.get("kind") == "entry" and d.get("path") == str(src):
                    e = d.get("entry")
                    if e:
                        sel_keys.add((e.date_str, e.title))
            if not sel_keys:
                # fallback: current entry
                if self.current_entry:
                    sel_keys.add((self.current_entry.date_str, self.current_entry.title))
            to_move = [e for e in entries if (e.date_str, e.title) in sel_keys]
            if not to_move:
                QMessageBox.warning(self, "Archive", "Select entries in tree (Ctrl+click) or pick current entry"); return
        elif mode == 1:  # previous month
            from datetime import datetime as dt
            cur = dt.now()
            prev_m = cur.month - 1 if cur.month > 1 else 12
            prev_y = cur.year if cur.month > 1 else cur.year - 1
            for e in entries:
                d = news_parser.parse_date(e.date_str)
                if d and d.year == prev_y and d.month == prev_m:
                    to_move.append(e)
        elif mode == 2:  # by month
            mk = params["month_key"]  # "2026-07"
            if mk:
                y, m = map(int, mk.split("-"))
                for e in entries:
                    d = news_parser.parse_date(e.date_str)
                    if d and d.year == y and d.month == m:
                        to_move.append(e)
        elif mode == 3:  # older than date
            cutoff = params["cutoff"]
            for e in entries:
                d = news_parser.parse_date(e.date_str)
                if d and d.date() < cutoff:
                    to_move.append(e)
        elif mode == 4:  # keep last N
            n = params["keep_n"]
            # entries are in file order (newest first after our fix). Use that order.
            if len(entries) > n:
                to_move = entries[n:]  # archive older ones
        if not to_move:
            QMessageBox.information(self, "Archive", "No entries match criteria (nothing to archive)"); return
        # Auto target if not set: based on first to_move month (keeps tags — to_move entries already have tags)
        if target is None:
            # For mixed months, we will group by month: if to_move spans multiple months, archive each month separately
            by_month = {}
            for e in to_move:
                d = news_parser.parse_date(e.date_str)
                if d:
                    k = f"{d.year}_{d.strftime('%m')}"
                else:
                    k = "unknown"
                by_month.setdefault(k, []).append(e)
            if len(by_month) > 1:
                # multiple months: archive per month
                total = 0
                for k, grp in by_month.items():
                    if k == "unknown":
                        tgt = Path(f"README_archived_{k}.md")
                    else:
                        y, mo = k.split("_")
                        tgt = Path(f"README_{y}_{mo}.md")
                    res = news_parser.archive_entries(src, grp, tgt, update_index=True)
                    total += res["moved"]
                    # reload entries for next iteration (src shrinks)
                    if res["moved"]:
                        content = src.read_text(encoding="utf-8")
                        entries = news_parser.parse_entries(content, str(src))
                QMessageBox.information(self, "Archived", f"Archived {total} entries from {src.name} (by month, tags preserved) → monthly files + README_ARCHIVE.md updated")
                self.rebuild_tree()
                return
            else:
                k = list(by_month.keys())[0]
                if k != "unknown":
                    y, mo = k.split("_")
                    target = Path(f"README_{y}_{mo}.md")
        res = news_parser.archive_entries(src, to_move, target, update_index=True)
        QMessageBox.information(self, "Archived", f"Archived {res['moved']} entries from {src.name} → {res['archive_path']} (now {res['archive_total']} entries).\nSource now {res['source_remaining']} entries.\nTags preserved, README_ARCHIVE.md updated.")
        self.rebuild_tree()

    def _write_entries_back(self, path: Path, entries, original_content: str):
        """Rewrite README file preserving header/footer around entries."""
        # Header is everything before first detected header
        lines = original_content.splitlines()
        # find first header line that is news entry
        first_h = None
        for i, l in enumerate(lines):
            if re.match(r'^#{1,2}\s+', l) and re.search(r'\b\d{4}\b', l) and re.search(r'[—–\-]', l):
                first_h = i
                break
        header = "\n".join(lines[:first_h]).strip() if first_h is not None else ""
        # Footer: after last separator (look for final div)
        # We just take header + entries separated by \n\n---\n\n + footer if exists (trailing divs)
        # Detect footer: content after last entry's separator block in original
        footer = ""
        # If original had a footer div like "<div align=center>" at end, keep it
        if "<div align=\"center\">" in original_content and original_content.rstrip().endswith("</div>"):
            # crude: last <div ...> block
            last_div_start = original_content.rfind("<div align=\"center\">")
            # check if after last separator there is this div and it's not inside an entry
            # If entries don't contain that div, treat as footer
            if last_div_start != -1:
                # ensure not already in entries
                footer_candidate = original_content[last_div_start:].strip()
                # Check if footer_candidate contains no news header
                if not re.search(r'^## .+\d{4}\s*[—–\-]', footer_candidate, re.MULTILINE):
                    footer = "\n\n" + footer_candidate

        # Build new content
        parts = []
        if header:
            parts.append(header.strip())
        for e in entries:
            parts.append(e.to_markdown())
        new_content = "\n\n---\n\n".join(parts)
        if footer:
            new_content += footer
        new_content += "\n"
        # Final normalization
        new_content = news_parser.normalize_file_content(new_content)
        path.write_text(new_content, encoding="utf-8")

    def save_current(self):
        # Detail file mode
        if self.current_detail_path is not None:
            p = self.current_detail_path
            txt = self.ed_body.toPlainText()
            p.write_text(txt, encoding="utf-8")
            self.statusBar().showMessage(f"Saved {p} ({len(txt)} chars)")
            QMessageBox.information(self, "Saved", f"Saved {p}")
            self.rebuild_tree()
            return

        # README entry mode
        if self.current_path is None:
            QMessageBox.warning(self, "No target", "Select a file/category in tree first"); return
        if self.current_path.is_dir():
            QMessageBox.warning(self, "Pick file", "Select a README file or entry, not a directory"); return
        if not self.current_path.exists() or self.current_path.suffix != ".md":
            QMessageBox.warning(self, "Invalid target", f"Target {self.current_path} is not a markdown file"); return

        # Validate
        if not self.ed_date.text().strip() or not self.ed_title.text().strip():
            QMessageBox.warning(self, "Missing", "Date and Title required"); return

        content = self.current_path.read_text(encoding="utf-8")
        entries = news_parser.parse_entries(content, source_file=str(self.current_path))

        # Build edited entry
        new_entry = news_parser.NewsEntry(
            raw_header=f"## {self.ed_date.text().strip()} — {self.ed_title.text().strip()}",
            header_level="##",
            date_str=self.ed_date.text().strip(),
            title=self.ed_title.text().strip(),
            emoji=self.ed_emoji.text().strip(),
            tags=self.ed_tags.text().strip(),
            body=self.ed_body.toPlainText().strip(),
            key_insight=self.ed_insight.text().strip(),
            links=[],
            source_file=str(self.current_path),
            category=self.current_path.stem.lower(),
        )
        # if link field set, inject into body if not already present
        link_txt = self.ed_link.text().strip()
        if link_txt and link_txt not in new_entry.body:
            # append as markdown link line
            new_entry.body += f"\n\n📖 **Full details:** [{Path(link_txt).stem}]({link_txt})"
            new_entry.links.append((Path(link_txt).stem, link_txt))

        if self.current_entry_index is not None and 0 <= self.current_entry_index < len(entries):
            entries[self.current_entry_index] = new_entry
        else:
            # new entry: prepend (newest first)
            entries.insert(0, new_entry)

        self._write_entries_back(self.current_path, entries, content)
        self.statusBar().showMessage(f"Saved {self.current_path.name} — {len(entries)} entries")
        QMessageBox.information(self, "Saved", f"Saved {self.current_path.name} with {len(entries)} entries")
        self.rebuild_tree()

    def update_preview(self, detail_mode=False):
        # Build preview markdown from current form
        date = self.ed_date.text().strip()
        title = self.ed_title.text().strip()
        emoji = self.ed_emoji.text().strip()
        tags = self.ed_tags.text().strip()
        body = self.ed_body.toPlainText().strip()
        insight = self.ed_insight.text().strip()
        link = self.ed_link.text().strip()

        if detail_mode or (self.current_detail_path is not None):
            # detail preview: just body rendered as markdown-ish
            html = f"<h3>{title}</h3><pre>{body[:4000]}</pre>"
            self.preview.setHtml(html)
            return

        if not date and not title and not body:
            self.preview.clear()
            return

        parts = []
        if date or title:
            hdr = f"{emoji + ' ' if emoji else ''}{date} — {title}" if date else title
            parts.append(f"<h2>{hdr}</h2>")
        if tags:
            parts.append(f"<p><i>{tags}</i></p>")
        if body:
            # simple markdown to html: preserve bullets, links, <br>, <a>
            body_html = body.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            # restore allowed tags
            for tag in ["<br>", "<a ", "</a>", "<b>", "</b>", "<i>", "</i>"]:
                body_html = body_html.replace(tag.replace("<","&lt;"), tag)
            body_html = re.sub(r'&lt;a href="([^"]+)"&gt;(.*?)&lt;/a&gt;', r'<a href="\1">\2</a>', body_html)
            body_html = body_html.replace("&lt;br&gt;", "<br>")
            # bullets: lines starting with -
            lines = body_html.splitlines()
            out = []
            in_ul = False
            for l in lines:
                ls = l.strip()
                if ls.startswith("- "):
                    if not in_ul:
                        out.append("<ul>"); in_ul = True
                    out.append(f"<li>{ls[2:]}</li>")
                else:
                    if in_ul:
                        out.append("</ul>"); in_ul = False
                    if ls:
                        out.append(f"<p>{l}</p>")
            if in_ul:
                out.append("</ul>")
            parts.append("\n".join(out))
        if insight:
            parts.append(f"<p><b>Key insight:</b> {insight}</p>")
        if link:
            parts.append(f'<p>📖 <a href="{link}">{link}</a></p>')
        self.preview.setHtml("\n<hr>\n".join(parts))

    # --- Ollama ---
    def refresh_server_combo(self):
        self.server_combo.blockSignals(True)
        self.server_combo.clear()
        for s in self.cfg["ollama_servers"]:
            self.server_combo.addItem(f'{s["name"]} — {s["url"]}', s["url"])
        # select active
        for i, s in enumerate(self.cfg["ollama_servers"]):
            if s["url"] == self.cfg["active_server"]:
                self.server_combo.setCurrentIndex(i); break
        self.server_combo.blockSignals(False)

    def on_server_changed(self, idx):
        if idx < 0: return
        url = self.server_combo.currentData()
        self.cfg["active_server"] = url
        save_config(self.cfg)
        self.refresh_models()

    def on_model_changed(self, txt):
        self.cfg["model"] = txt.strip()
        save_config(self.cfg)

    def manage_servers(self):
        dlg = ServerDialog(self.cfg, self)
        dlg.exec_()
        self.refresh_server_combo()
        save_config(self.cfg)

    def test_connection(self):
        url = self.cfg["active_server"]
        try:
            r = requests.get(f"{url.rstrip('/')}/api/tags", timeout=4)
            r.raise_for_status()
            QMessageBox.information(self, "Ollama", f"Connected to {url}\nModels: {len(r.json().get('models',[]))} found")
        except Exception as e:
            QMessageBox.warning(self, "Ollama offline", f"Cannot reach {url}\n{e}\n\nEditor still works offline.")

    def refresh_models(self):
        url = self.cfg.get("active_server", "http://localhost:11434")
        self.model_combo.setPlaceholderText("loading models...")
        self._mw = OllamaModelsWorker(url)
        self._mw.result.connect(self._on_models)
        self._mw.error.connect(lambda e: self.statusBar().showMessage(f"Ollama offline at {url}: {e} — offline mode"))
        self._mw.start()

    def _on_models(self, models):
        cur = self.cfg.get("model", "")
        self.model_combo.blockSignals(True)
        self.model_combo.clear()
        for m in models:
            self.model_combo.addItem(m)
        if cur and cur not in models:
            self.model_combo.addItem(cur)
        if cur:
            idx = self.model_combo.findText(cur)
            if idx >= 0:
                self.model_combo.setCurrentIndex(idx)
        self.model_combo.blockSignals(False)
        self.statusBar().showMessage(f"Ollama {self.cfg['active_server']} — {len(models)} models")

    def _current_context(self) -> str:
        # selected file content + current form state
        ctx = ""
        if self.current_path and self.current_path.exists() and self.current_path.is_file():
            try:
                ctx = self.current_path.read_text(encoding="utf-8")[:6000]
            except:
                pass
        # add form body
        ctx += f"\n\n---Current edit---\nDate: {self.ed_date.text()}\nTitle: {self.ed_title.text()}\nTags: {self.ed_tags.text()}\nBody:\n{self.ed_body.toPlainText()}\nInsight: {self.ed_insight.text()}\n"
        return ctx

    def send_ai(self, preset: str | None):
        txt = self.ai_input.toPlainText().strip() if preset is None else preset
        if not txt:
            QMessageBox.information(self, "Empty", "Write a prompt or click a quick button"); return
        server = self.cfg.get("active_server", "http://localhost:11434")
        model = self.cfg.get("model", "") or self.model_combo.currentText().strip()
        if not model:
            QMessageBox.warning(self, "No model", "Select a model (e.g. qwen2.5:7b) in top bar"); return

        # if preset, append body context
        if preset is not None and self.ed_body.toPlainText().strip():
            txt = preset + "\n\nEntry body:\n" + self.ed_body.toPlainText().strip()[:3000]
            if self.ed_title.text().strip():
                txt = f"Title: {self.ed_title.text().strip()}\n" + txt

        self.ai_history.append(f"<b>You:</b> {txt}<hr>")
        self.ai_input.clear()
        self.btn_send.setEnabled(False)
        self.btn_send.setText("Thinking...")
        self.statusBar().showMessage(f"Asking {model} @ {server}...")

        ctx = self._current_context()
        self.ollama_worker = OllamaWorker(server, model, txt, ctx)
        # accumulate streaming into last block
        self._ai_buffer = ""
        self.ollama_worker.chunk.connect(self.on_ai_chunk)
        self.ollama_worker.finished_ok.connect(self.on_ai_done)
        self.ollama_worker.error.connect(self.on_ai_error)
        self.ollama_worker.start()
        # start new block
        self.ai_history.append("<b>AI:</b> ")
        self._ai_cursor = self.ai_history.textCursor()
        self._ai_cursor.movePosition(self._ai_cursor.End)

    def on_ai_chunk(self, text):
        self._ai_buffer += text
        self.last_ai_text = self._ai_buffer
        # append to history (simple: move cursor and insert)
        cursor = self.ai_history.textCursor()
        cursor.movePosition(cursor.End)
        cursor.insertText(text)
        self.ai_history.setTextCursor(cursor)
        self.ai_history.ensureCursorVisible()

    def on_ai_done(self):
        self.btn_send.setEnabled(True)
        self.btn_send.setText("Send to Ollama ▶")
        self.statusBar().showMessage("AI done — click Apply to use suggestion")
        self.ai_history.append("<hr>")

    def on_ai_error(self, msg):
        self.btn_send.setEnabled(True)
        self.btn_send.setText("Send to Ollama ▶")
        self.ai_history.append(f"<i style='color:red'>Error: {msg}</i><hr>")
        self.statusBar().showMessage(f"Ollama error: {msg} — check server {self.cfg['active_server']}")

    def apply_ai_to_fields(self):
        if not self.last_ai_text or not self.last_ai_text.strip():
            QMessageBox.information(self, "No AI", "No AI text to apply. Ask AI first."); return
        # Heuristic: if AI returned markdown entry, try to parse title/body
        txt = self.last_ai_text.strip()
        # Let user choose what to apply
        choice, ok = QInputDialog.getItem(self, "Apply AI", "What to apply?", ["Append to Body", "Replace Body", "Set Title", "Set Insight", "Show in dialog"], 0, False)
        if not ok: return
        if choice == "Append to Body":
            self.ed_body.setPlainText(self.ed_body.toPlainText().rstrip() + "\n\n" + txt)
        elif choice == "Replace Body":
            self.ed_body.setPlainText(txt)
        elif choice == "Set Title":
            # first line as title if short
            title = txt.splitlines()[0].strip()[:120]
            self.ed_title.setText(title)
        elif choice == "Set Insight":
            self.ed_insight.setText(txt.splitlines()[0].strip()[:300])
        else:
            dlg = QDialog(self); dlg.setWindowTitle("AI output"); dlg.resize(700, 500)
            lay = QVBoxLayout(dlg); te = QPlainTextEdit(txt); te.setReadOnly(True); lay.addWidget(te)
            bb = QDialogButtonBox(QDialogButtonBox.Close); bb.rejected.connect(dlg.reject); lay.addWidget(bb)
            dlg.exec_()
        self.update_preview()


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
