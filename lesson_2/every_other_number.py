# A function that takes a list of integers, and returns a new list with every 
# other element from the original list, starting with the first element.

# START
# Given a list of numbers

# SET new_numbers = empty list 
# SET iterator = 1

# WHILE iterator <= length of list 
# SET current_number = number in list at position iterator

# IF current_number is an odd number
#   SET new_numbers = new_numbers + current_number

# SET iterator = iterator + 1

# PRINT new_numbers

def every_other(list):
    new_numbers = []
    iterator = 0

    while iterator < len(list):
        current_number = list[iterator]
        if current_number % 2 != 0:
            new_numbers.append(current_number)
        
        iterator += 1
    
    print(new_numbers)

every_other([1,4,7,2,5])