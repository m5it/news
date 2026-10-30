#!/bin/bash
# News Editor launcher — lightweight, works on weak PCs
# Uses user-local PyQt5 if system pip is blocked (PEP 668)
DIR="$(cd "$(dirname "$0")" && pwd)"
export PYTHONPATH="$HOME/.local/lib/python3.13/site-packages:$PYTHONPATH"
export QT_QPA_PLATFORM=${QT_QPA_PLATFORM:-xcb}
# If no display, try offscreen for testing
if [ -z "$DISPLAY" ] && [ -z "$WAYLAND_DISPLAY" ]; then
  echo "No display detected — run with xvfb or set DISPLAY"
  echo "Example: xvfb-run python3 news_editor.py"
fi
exec python3 "$DIR/bin/news_editor.py" "$@"
