import subprocess
import os

# --- SETTINGS ---
SCRIPT_NAME = "main.py"          # Your actual python file
APP_NAME = "Simple_Calc"         # The name of the final .exe
ICON_FILE = "calculaterPicture.ico" # Make sure the spelling matches!
# ----------------

def build_exe():
    # Check if icon exists to prevent PyInstaller errors
    if not os.path.exists(ICON_FILE):
        print(f"Warning: {ICON_FILE} not found. Build might fail or use default icon.")

    # Construct the command
    command = [
        "python", "-m", "PyInstaller",
        "--onefile",              # Create a single EXE
        "--console",              # makes sure there is a black box
        f"--name={APP_NAME}",     # Name of the output file
        f"--icon={ICON_FILE}",    # Path to the icon
        "--clean",                # Clear temporary files before building
        SCRIPT_NAME
    ]

    print(f"Building {APP_NAME}...")
    
    # Run the command
    result = subprocess.run(command)

    if result.returncode == 0:
        print("\nBuild Successful! Check the 'dist' folder for your EXE.")
    else:
        print("\nBuild Failed. Check the error messages above.")

if __name__ == "__main__":
    build_exe()