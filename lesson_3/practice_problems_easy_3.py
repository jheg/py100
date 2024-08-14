# Question 1
# Write two different ways to remove all of the elements from the following 
# list

numbers = [1, 2, 3, 4]

while numbers:
    numbers.pop()

print(numbers)

numbers = [1, 2, 3, 4]

for num in range(len(numbers)):
    numbers.pop()

print(numbers)

numbers = [1, 2, 3, 4]
numbers.clear()

print(numbers)

# Question 2
# What will the following code output?

print([1, 2, 3] + [4, 5])       # [1, 2, 3, 4, 5]

# Question 3
# What will the following code output?

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1)                     # Hello there

# Question 4
# What will the following code output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()      # Makes a shallow copy meaning the dictionaries
# point to a location in memory
my_list2[0]['first'] = 42
print(my_list1)                 # [{"first": 42}, {"second": "value2"}, 3, 4, 5]

# Question 5
# The following function unnecessarily uses two return statements to return 
# boolean values. Can you rewrite this function so it only has one return 
# statement and does not explicitly use either True or False?

def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False

# Try to come up with two different solutions.

def is_the_color_valid(color):
    return color == "blue" or color == "green"

print(is_the_color_valid('yellow'))
print(is_the_color_valid('green'))

def is_this_color_valid(color):
    return color in ["blue", "green"]

print(is_this_color_valid('yellow'))
print(is_this_color_valid('green'))