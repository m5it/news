In **tmux**, you can split a window into multiple panes (vertical or horizontal) and later restore the original layout. Here's how to do it:                                                
                                                                                                                                                                                            
---                                                                                                                                                                                         
                                                                                                                                                                                            
### **1. Splitting a Window**                                                                                                                                                               
#### **Vertical Split** (left-right)                                                                                                                                                        
```sh                                                                                                                                                                                       
Ctrl-b + "                                                                                                                                                                                  
```                                                                                                                                                                                         
- Press `Ctrl-b` (tmux prefix), then `"` (double quote).                                                                                                                                    
                                                                                                                                                                                            
#### **Horizontal Split** (top-bottom)                                                                                                                                                      
```sh                                                                                                                                                                                       
Ctrl-b + %                                                                                                                                                                                  
```                                                                                                                                                                                         
- Press `Ctrl-b`, then `%`.                                                                                                                                                                 
                                                                                                                                                                                            
---                                                                                                                                                                                         
                                                                                                                                                                                            
### **2. Navigating Between Panes**                                                                                                                                                         
- **Switch to next pane** (right/down): `Ctrl-b + o`                                                                                                                                        
- **Switch to previous pane** (left/up): `Ctrl-b + ;`                                                                                                                                       
- **Move focus to specific pane** (e.g., pane 1, 2, 3, 4):                                                                                                                                  
  - `Ctrl-b + {1,2,3,4}` (if you have 4 panes).                                                                                                                                             
                                                                                                                                                                                            
---                                                                                                                                                                                         
                                                                                                                                                                                            
### **3. Resizing Panes**                                                                                                                                                                   
- **Increase pane size** (current direction):                                                                                                                                               
  - `Ctrl-b + :` → `resize-pane -L` (left/up)                                                                                                                                               
  - `Ctrl-b + :` → `resize-pane -R` (right/down)                                                                                                                                            
- **Decrease pane size**:                                                                                                                                                                   
  - `Ctrl-b + :` → `resize-pane -r` (right/down)                                                                                                                                            
  - `Ctrl-b + :` → `resize-pane -U` (left/up)                                                                                                                                               
                                                                                                                                                                                            
---                                                                                                                                                                                         

### **4. Restoring the Original Layout**
#### **Option 1: Close All Panes Except One**
1. **Kill all panes except the one you want**:
   - `Ctrl-b + x` (kill pane) → repeat for all but the desired one.
   - **Warning**: This permanently closes other panes.                                                                                                                                      
                                                                                                                                                                                            
#### **Option 2: Save & Restore Layout (Recommended)**                                                                                                                                      
1. **Save the current layout** (e.g., to `layout.json`):                                                                                                                                    
   ```sh                                                                                                                                                                                    
   tmux save-layout -S layout.json                                                                                                                                                          
   ```                                                                                                                                                                                      
2. **Restore the layout later**:                                                                                                                                                            
   ```sh                                                                                                                                                                                    
   tmux load-layout -S layout.json                                                                                                                                                          
   ```                                                                                                                                                                                      
   - Or reload it in the same session:                                                                                                                                                      
     ```sh                                                                                                                                                                                  
     tmux source-file layout.json                                                                                                                                                           
     ```                                                                                                                                                                                    
                                                                                                                                                                                            
#### **Option 3: Reset to Single Pane (Discard Splits)**                                                                                                                                    
- **Close all panes** (except current):                                                                                                                                                     
  ```sh                                                                                                                                                                                     
  tmux kill-pane -a                                                                                                                                                                         
  ```                                                                                                                                                                                       
- **Or split off the current pane** (leaving a single pane):                                                                                                                                
  ```sh                                                                                                                                                                                     
  tmux split-window -h  # horizontal                                                                                                                                                        
  tmux split-window -v  # vertical                                                                                                                                                          
  ```                                                                                                                                                                                       
  Then close the new pane (`Ctrl-b + x`).                                                                                                                                                   
                                                                                                                                                                                            
---                                                                                                                                                                                         
                                                                                                                                                                                            
### **5. Alternative: Use `tmux-prefix + q` to See Layout**                                                                                                                                 
- Press `Ctrl-b + q` to see pane numbers (useful for navigation).

---

### **Summary**
| Action | Command |
|--------|---------|
| **Vertical split** | `Ctrl-b + "` |
| **Horizontal split** | `Ctrl-b + %` |
| **Kill all panes except current** | `Ctrl-b + x` (repeat) |
| **Save layout** | `tmux save-layout -S layout.json` |
| **Restore layout** | `tmux load-layout -S layout.json` |
