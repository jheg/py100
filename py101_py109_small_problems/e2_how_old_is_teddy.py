"""
How Old is Teddy?
Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.
"""
import random

def how_old_is_teddy(name="Teddy"):
    return f"{name} is {random.randrange(20,100)} years old."

print(how_old_is_teddy("John"))     # John is ... years old.
print(how_old_is_teddy())           # Teddy is ... years old