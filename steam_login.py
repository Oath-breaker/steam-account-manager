import pyautogui, subprocess, time, sys, json, urllib.request


# Checks if there is any accounts in login.data
# If exists, continue, else terminate with 'No active accounts found'
try:
    with open('C:\\Users\\user\\Desktop\\Steam_Automation\\login.data', 'r') as d:
        credentials = credentials[uid]
    d.close()
    
    
    pyautogui.FAILSAFE = True
    # Get steam.exe path and launch it
    print('Launching Steam.exe...')
    path = ['C:\\Program Files (x86)\\Steam\\Steam.exe']
    run_prog = subprocess.Popen(path)
    
    time.sleep(3)
    # Automation
    
    print("1 active account found. Getting it's credentials..")
    time.sleep(1)
    print("Uid of account founded is, "+credentials[0])
    time.sleep(1)

    x, y = 960, 455 # Get coordintates of username input
    pyautogui.doubleClick(x, y, button='left')
    pyautogui.typewrite(credentials[1])
    print('Entering username... ')
    
    time.sleep(1)
    
    x, y = 960, 489 # Get coordinates of password input
    pyautogui.click(x, y, clicks=1, button='left')
    pyautogui.typewrite(credentials[2])
    print('Entering password...')
    pyautogui.typewrite(['enter'])
    time.sleep(1)
	
except FileNotFoundError:
    credentials = ["","",""]
    print("No active accounts found. Make sure you have at least 1 account setup as active.")

# End
sys.exit(0)		