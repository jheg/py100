"""
ddaaiillyy ddoouubbllee
Write a function that takes a string argument and returns a new string that contains the value of the original string with 
all consecutive duplicate characters collapsed into a single character.
"""

def crunch(str):
    chars = []
    previous_char = ''

    for char in str:
        if char != previous_char:    
            chars.append(char)
        previous_char = char


    return ''.join(chars)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')