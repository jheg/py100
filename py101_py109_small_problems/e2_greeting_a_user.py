"""
Greeting a user
Write a program that asks for user's name, then greets the user. 
If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).
"""

def greet_user():
    name = input("What is your name? ")
    if name[-1] == "!":
        print(f"HELLO {name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {name}.")

greet_user()