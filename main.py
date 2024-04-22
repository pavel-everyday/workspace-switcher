from pynput.mouse import Listener
import subprocess
from throttle import CoolDown

TOP_BUTTON_NEAR_HORIZONTAL_SCROLL = 'button9'
BOTTOM_BUTTON_NEAR_HORIZONTAL_SCROLL = 'button8'

# return info bout the workspaces:
# 0  - DG: 2560x1600  VP: N/A  WA: 66,27 2494x1573  Workspace 1
# 1  * DG: 2560x1600  VP: 0,0  WA: 66,27 2494x1573  
# 2  - DG: 2560x1600  VP: N/A  WA: 66,27 2494x1573  N/A
def get_workspace_info():
    result = subprocess.run(["wmctrl", "-d"], stdout=subprocess.PIPE)
    stinfo_string = result.stdout
    return str(stinfo_string)

def get_current_workspace(info_str: str):
    markIndex = info_str.find("*")
    workspace_index = info_str[markIndex - 3]
    return int(workspace_index)

def get_workspaces_amount(info_str: str):
    amount = info_str.count("DG:")
    return amount

@CoolDown(0.1)
def move_to_next_workspace():
    info_str = get_workspace_info()
    current_ws_index = get_current_workspace(info_str)
    amount = get_workspaces_amount(info_str)
    is_next_workspace = current_ws_index < (amount - 1)
    
    if is_next_workspace:
        next_index = str(current_ws_index + 1) 
        subprocess.run(["wmctrl", "-s", next_index])

@CoolDown(0.1)
def move_to_previous_workspace():
    info_str = get_workspace_info()
    current_ws_index = get_current_workspace(info_str)
    is_previous_workspace = current_ws_index > 0
    
    if is_previous_workspace:
        next_index = str(current_ws_index - 1) 
        subprocess.run(["wmctrl", "-s", next_index])

def on_click(x, y, button, pressed):
    if(((button.name == TOP_BUTTON_NEAR_HORIZONTAL_SCROLL) & pressed)):
        #  move to next and redefine the workspaces
        move_to_next_workspace()
    if((button.name == BOTTOM_BUTTON_NEAR_HORIZONTAL_SCROLL) & pressed):
        #  move to previous and redefine the workspaces
        move_to_previous_workspace()

with Listener(on_click=on_click) as listener:
    listener.join()


