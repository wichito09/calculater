import subprocess
import sys
import os


# instructions for first time using it, delete it after
'''
This is an application builder for python, below you can change the stuff to better suit your project, 
down in the command varible you can change, delete, or add flags to better suit your needs. If your python
project uses a GUI and not the console, you can replace the '--console' for 'noconsole', you can remove 
the '--onefile' if your project needs other files. 

THIS ONLY WORKS FOR PYTHON, I REAPEAT ONLY FOR PYTHON.

This code was MADE BY AI and not by me since I have no idea what subprocess is or what sys or os does.

you can copy this code and put it in your project folder. 
'''
# instructions for future use, DO NOT DELETE you may forget
'''
make sure flags suit your current needs, double check settings are okay, make sure your .py
file where your main code is in is in the same folder as this file and the .ICO is also in the same said folder.

Version 1.0 
80% Ai - 15% me - 5% internet
'''


# --- SETTINGS ---
current_folder_name = os.path.basename(os.getcwd())

SCRIPT_NAME = "main.py"  # add the script name you want to turn into a program Ex. ("main.py")
APP_NAME = current_folder_name # The name of the app 
ICON_FILE = "calculaterPicture.ico" # The icon the app should have, .ico, has to be in same file as SCRIPT_NAME and this one
# ----------------

def ensure_pyinstaller(): # checks if pyinstaller is installed if not attempts to install it
    try:
        import PyInstaller
        print("PyInstaller is already installed.")
    except ImportError:
        print("PyInstaller not found. Attempting to install...")
        try:
            # This runs 'python -m pip install pyinstaller'
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
            print("Successfully installed PyInstaller!")
        except Exception as e:
            print(f"Failed to install PyInstaller: {e}")
            sys.exit(1)

def build_exe(): # builds the app
    ensure_pyinstaller()

    if not os.path.exists(ICON_FILE): # checks if icon_file exist
        print(f"Warning: {ICON_FILE} not found. Proceeding without custom icon.")
        icon_flag = []
    else:
        icon_flag = [f"--icon={ICON_FILE}"]

   
    command = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console", 
        f"--name={APP_NAME}",
        "--clean"
    ] + icon_flag + [SCRIPT_NAME] # puts the command all together

    print(f"\nBuilding {APP_NAME}...")
    result = subprocess.run(command)

    if result.returncode == 0:
        print(f"\nSuccess! Your EXE is in the 'dist' folder.")
    else:
        print("\nBuild failed. Check the errors above.")

if __name__ == "__main__":
    build_exe()