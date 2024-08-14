# X Question 1
# Write two distinct ways of reversing the list 
# without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

print(list(reversed(numbers)))
print(sorted(numbers, reverse=True))
print(numbers[::-1])
print(numbers)

# Question 2 
# Given a number and a list, determine whether the number 
# is included in the list.

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# X Question 3 
# Programmatically determine whether 42 lies between 10 and 100, inclusive. 
# Do the same for the values 100 and 101.

print('if/else')
if 10 < 42 < 100: 
    print(True)
else: 
    print(False)

if 100 < 100 < 100: 
    print(True)
else: 
    print(False)

if 100 < 101 < 100: 
    print(True)
else: 
    print(False)
print('-')

print('Comprehension')
print(True if (10 < 42 < 100) else False)
print(True if (10 < 100 < 100) else False)
print(True if (10 < 101 < 100) else False)
print('-')

print('Using range()')
print(42 in range(10,100))
print(100 in range(10,100))
print(101 in range(10,100))
print('-')

# X Question 4
# Given a list of numbers [1, 2, 3, 4, 5], mutate the list by removing the 
# number at index 2, so that the list becomes [1, 2, 4, 5].

q4_numbers = [1, 2, 3, 4, 5]

q4_numbers.pop(2)   # returns the removed element 
print(q4_numbers)

del q4_numbers[2]   # does not return the removed element. Can also use slicing
print(q4_numbers)

q4_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del q4_numbers[0:9:2]

print(q4_numbers)

# X Question 5
# How would you verify whether the data structures assigned to the variables 
# numbers and table are of type list?

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print(type(numbers))
print(type(table))

# Checks if is an instance of a class OR sub-class
print(isinstance(numbers, list))
print(isinstance(table, list))

# Also works but has potential issues as is strict. For example, returns False
# if the object is a sub-class that inherits from list
# Less pyhtonic. Python encourages duck typing which means to check for 
# behaviour rather than specific types
type(numbers) is list      # True
type(table) is list        # False

# Question 6 
# Back in the stone age (before CSS), we used spaces to align things on 
# the screen. If we have a 40-character wide table of Flintstone family 
# members, how can we center the following title above the table with spaces?

# Calculate the length of title
# Assign to diff the result of subtracting length from 40
# Assign to div the reuslt of dividing by 2 using integer division
# Concatinate div spaces and title 

title = "Flintstone Family Members"

# Me
spaces = (40 - len(title)) // 2
print("-" * 40)
print(f'{" " * spaces}{title}')

# Solution
centered_title = title.center(40)
print(centered_title)

# Question 7 
# Write a one-liner to count the number of lower-case t characters in each of 
# the following strings:

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

# Question 8
# Determine whether the following dictionary of people and their age contains 
# an entry for 'Spot':

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print('Spot' in ages)

# Question 9
# We have most of the Munster family in our ages dictionary:

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

# Add entries for Marilyn and Spot to the dictionary:

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
print(ages)

