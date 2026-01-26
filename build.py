import subprocess
import sys
import os

# --- SETTINGS ---
SCRIPT_NAME = "main.py"
APP_NAME = "Simple_Calc"
ICON_FILE = "calculaterPicture.ico"
# ----------------

def ensure_pyinstaller():
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

def build_exe():
    ensure_pyinstaller()

    if not os.path.exists(ICON_FILE):
        print(f"Warning: {ICON_FILE} not found. Proceeding without custom icon.")
        icon_flag = []
    else:
        icon_flag = [f"--icon={ICON_FILE}"]

    # Note: Using --console because your app uses input() 
    # This prevents the 'lost sys.stdin' error.
    command = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",
        "--console", 
        f"--name={APP_NAME}",
        "--clean"
    ] + icon_flag + [SCRIPT_NAME]

    print(f"\nBuilding {APP_NAME}...")
    result = subprocess.run(command)

    if result.returncode == 0:
        print(f"\nSuccess! Your EXE is in the 'dist' folder.")
    else:
        print("\nBuild failed. Check the errors above.")

if __name__ == "__main__":
    build_exe()