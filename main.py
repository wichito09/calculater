import sys
import time
# all the imports we need up here


VERSION = 0.1
    # never changing variables

def logoV(): # stuff to know
    print("""
 /$$      /$$ /$$           /$$                  /$$$$$$   /$$$$$$ 
| $$  /$ | $$|__/          | $$                 /$$$_  $$ /$$__  $$
| $$ /$$$| $$ /$$  /$$$$$$$| $$$$$$$   /$$$$$$ | $$$$\ $$| $$  \ $$
| $$/$$ $$ $$| $$ /$$_____/| $$__  $$ /$$__  $$| $$ $$ $$|  $$$$$$$
| $$$$_  $$$$| $$| $$      | $$  \ $$| $$  \ $$| $$\ $$$$ \____  $$
| $$$/ \  $$$| $$| $$      | $$  | $$| $$  | $$| $$ \ $$$ /$$  \ $$
| $$/   \  $$| $$|  $$$$$$$| $$  | $$|  $$$$$$/|  $$$$$$/|  $$$$$$/
|__/     \__/|__/ \_______/|__/  |__/ \______/  \______/  \______/ """)
    
    print(f"Version {VERSION}")

logoV()

time.sleep(2)

def greeting(): # gretting the user and stuff
    print("Hello this is a calculator")
    print("You will enter an operation")
    print("Then 2 numbers")
    print("Enjoy!")

greeting()

def main():
    oper = None
    x = None
    y = None
    ans = None
    # changing variables

    

    def add(x,y):
        return(x + y)

    def sub(x,y):
        return(x - y)

    def div(x,y):
        if not y == 0:
            return(x / y)
        else:
            None


    def mult(x,y):
        return(x * y)

    # all the functions for the operations-----------

    
    time.sleep(2)

    def oper_ask():
        valid_oper = ["add", "sub", "div", "mult"]
        while True:
            oper = input("please input an operation(Ex. add, sub, mult, div): ")       
            if oper in valid_oper:
                print("you chose", oper,"as your operation!")
                return(oper)
            else:
                print("ERROR, Invalid operation chosen. Try again")

    oper = oper_ask()
    time.sleep(1)

    def num1():
        while True:
            x = input("please input the first number!: ")
            try:
                x = int(x)
                return(x)
            except ValueError:
                print("ERROR, not a number please enter a number")
    x = num1()

    def num2():
        while True:
            y = input("please input the seccond number!: ")
            try:
                y = int(y)
                if y == 0 and oper == "div":
                    print("ERROR, can't divide by zero")
                else:
                    return(y)
            except ValueError:
                print("ERROR, not a number please enter a number")

    y = num2()

    print("You chose to do",oper,". Your first number was",x,", the seccond one was", y,".")
    if oper == "add":
        ans = add(x,y)
    elif oper == "sub":
        ans = sub(x,y)
    elif oper == "div":
        ans = div(x,y)
    elif oper == "mult":
        ans = mult(x,y)
    else:
        print("something broke :(")

    if oper == None or x == None or y == None:
        print("something broke :0")
    else:
        print("thinking...")
        time.sleep(1)
        print("carring the 1...")
        time.sleep(1)
        print("doing it one more time...")
        time.sleep(2)
        print("The ansear is", ans)
main()

time.sleep(2)

while True:
    user_input = input("Do you want to do another operation?(y/n): ")
    if user_input == "y":
        main()
    elif user_input == "n":
        print("bye bye")
        break
    else:
        print("invalid input")