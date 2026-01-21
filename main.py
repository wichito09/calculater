import time
VERSION = 0.1

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
    print(f"Version {VERSION}")

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
            return int(val)
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
        break