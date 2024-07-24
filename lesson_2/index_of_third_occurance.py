"""
A function that determines the index of the 3rd occurrence of a given 
character in a string. For instance, if the given character is 'x' and 
the string is 'axbxcdxex', the function should return 6 (the index of the 3rd 
'x'). If the given character does not occur at least 3 times, return None.
"""

# START
# Given a character and a string

# SET iterator = 1
# SET occurances = 0

# WHILE iterator <= number of characters in string
# SET current_character = character at position iterator    
# IF current_character = character
#   SET occurances = occurances + 1
#   IF occurances = 3
#       print iterator
# SET iterator = iterator + 1

# IF occurances < 3:
#   return None

def third_occurance(char, string):
    iterator = 0
    occurances = 0

    while iterator < len(string):
        current_character = string[iterator]
        if current_character == char:
            occurances += 1
            if occurances == 3:
                print(iterator)
        iterator += 1
        
    if occurances < 3:
        return None

third_occurance("x", "axbxcdxex")


