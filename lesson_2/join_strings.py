# a function that takes a list of strings, and returns a string that is all 
# those strings concatenated together

# START
# Given a list of strings

# SET iterator = 1
# SET longer_string = empty string

# WHILE iterator <= length of list
# SET current_string = string at position iterator

# SET longer_string = longer_string + current_string
# SET iterator = iterator + 1

# PRINT longer_string

def join_strings(list):
    iterator = 0
    longer_string = ''

    while iterator < len(list):
        current_string = list[iterator]
        longer_string = longer_string + current_string
        iterator += 1
    
    print(longer_string)

join_strings(['Jason', 'Lee', 'Hegarty', 'Victoria', 'Rance'])