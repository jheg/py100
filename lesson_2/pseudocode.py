"""
Keyword	            Meaning
START	            start of the program
SET	                set a variable that we can use for later
GET	                retrieve input from user
PRINT	            display output to user
READ	            retrieve a value from a variable
IF/ELSE IF/ELSE	    show conditional branches in logic
WHILE	            show looping logic
END	                end of the program
"""
# START
# Given a collection of numbers.

# SET iterator = 1
# SET savedNumber = value in numbers in position 0

# WHILE iterator <= length of numbers
# SET currentNumber = value within numbers collection at position iterator

# IF currentNumber > savedNumber 
#   savedNumber = currentNumber
# ELSE
#   skip to next number

# iterator = iterator + 1

# PRINT savedNumber

def greatestnumber(numbers):
    iterator = 0
    saved_number = numbers[0]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number
        iterator += 1
    
    print(saved_number)

greatestnumber([3,56,1,34])