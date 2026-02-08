import time
import requests
import sys


def check_for_updates(current_version, repo_owner, repo_name):
    """
    Checks GitHub for the latest release. 
    Returns (True, latest_url) if update exists, else (False, None).
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
        data = response.json()
        
        latest_version = data['tag_name'].lstrip('v')
        
        if latest_version != current_version:
 
            return True, data['html_url']
            
    except Exception:
        # Silently fail so the user isn't interrupted by network errors
        pass

    return False, None
    


__version__ = "1.5.0"
REPO_OWNER = "wichito09"
REPO_NAME = "calculater"

def start_app():
    # Check for update at the very start
    update_available, link = check_for_updates(__version__, REPO_OWNER, REPO_NAME)
    
    if update_available:
        print(f"[*] A new version is available! Download: {link}")
    
    print("Launching application...")
    # 1. Define all your "tools" (functions) at the top
    def logoV():
        # 'r' means "Raw" - ignores backslash mistakes
        print(r"""
    /$$      /$$ /$$           /$$                  /$$$$$$   /$$$$$$ 
    | $$   /$ | $$|__/          | $$                 /$$$_  $$ /$$__  $$
    | $$ /$$$| $$ /$$  /$$$$$$$| $$$$$$$   /$$$$$$ | $$$$\ $$| $$  \ $$
    | $$/$$ $$ $$| $$ /$$_____/| $$__  $$ /$$__  $$| $$ $$ $$|  $$$$$$$
    | $$$$_  $$$$| $$| $$      | $$  \ $$| $$  \ $$| $$\ $$$$ \____  $$
    | $$$/ \  $$$| $$| $$      | $$  | $$| $$  | $$| $$ \ $$$ /$$  \ $$
    | $$/   \  $$| $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/
    |__/     \__/|__/ \_______/|__/  |__/ \______/  \______/  \______/ """)
        
        # 'f' means "Fill-in-the-blanks"
        print(f"Version {__version__}")

    def add(x, y): return x + y
    def sub(x, y): return x - y
    def mult(x, y): return x * y
    def div(x, y): return x / y

    def oper_ask():
        valid_oper = ["add", "sub", "div", "mult"]
        while True:
            choice = input("Please input an operation (add, sub, mult, div): ").lower()      
            if choice in valid_oper:
                return choice
            else:
                print("ERROR: Invalid operation. Try again.")

    def get_num(label):
        while True:
            val = input(f"Please input the {label} number: ")
            try:
                return float(val)
            except ValueError:
                print("ERROR: Not a number. Try again.")

    # 2. The logic part of your program
    def main():
        logoV()
        time.sleep(1)
        
        print("Hello! Enter an operation and two numbers.\n")
        
        oper = oper_ask()
        x = get_num("first")
        
        # Special check for division by zero
        while True:
            y = get_num("second")
            if oper == "div" and y == 0:
                print("ERROR: You cannot divide by zero! Pick a different second number.")
            else:
                break

        print(f"You chose to {oper} {x} and {y}.")
        
        # Calculate the answer
        if oper == "add":
            ans = add(x, y)
        elif oper == "sub":
            ans = sub(x, y)
        elif oper == "div":
            ans = div(x, y)
        elif oper == "mult":
            ans = mult(x, y)

        print("Thinking...")
        time.sleep(1)
        print("Carrying the 1...")
        time.sleep(1)
        print(f"The answer is: {ans}\n")

    # 3. The "Keep Playing" loop
    while True:
        main()
        again = input("Do you want to do another operation? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    start_app()