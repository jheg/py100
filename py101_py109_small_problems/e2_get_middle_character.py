"""
Get Middle Character

Write a function that takes a non-empty string argument and returns the middle character(s) of the string. 
If the string has an odd length, you should return exactly one character. 
If the string has an even length, you should return exactly two characters.

- Determine odd or even
- Calc length of string
- if even return chars: length / 2 to length / 2 + 1
- if odd return char: length % 2 + 1
"""

def center_of(str):
    if len(str) % 2 == 0:
        return f'{str[len(str) // 2 - 1]}{str[len(str) // 2]}'
    else:
        return f'{str[len(str) // 2]}'                

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True