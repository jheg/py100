# Question 1
# Will the following functions return the same results?

def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# Yes however the second, whilst it will run is not pythonic.. wrong
# the second function returns None 

# These functions do not return the same thing. The function first() returns 
# the expected value of { prop1: "hi there" }, but second() returns None 
# without throwing any errors.

# In Python, if there's nothing after a return statement, the function will 
# return None. The indented block after the return statement in second 
# function is unreachable and doesn't affect the return value.

# Question 2
# What does the last line in the following code output?

dictionary = {'first': [1]}
num_list = dictionary['first']  # This references the same object as 
                                # dictionary['first']
num_list.append(2)

print(num_list)     # [1, 2]
print(dictionary)   # {'first': [1, 2]}

# If this behaviour was not desired then you can call the copy() method on 
# the mutable object
copy_of_list = dictionary['first'].copy()
copy_of_list.append(3)

print(copy_of_list)     # [1, 2, 3]
print(dictionary)       # {'first': [1, 2]}

# You can also use slice as it returns a new list. 
another_copy = dictionary['first'][:]
another_copy.append(4)
print(another_copy)     # [1, 2, 4]
print(dictionary)       # {'first': [1, 2]}

# Question 3
# Given the following similar sets of code, what will each code snippet print?

# 1st func
def mess_with_vars(one, two, three):
    one = two       # [two]
    two = three     # [three]
    three = one     # [two]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")         # ['one']
print(f"two is: {two}")         # ['two']
print(f"three is: {three}")     # ['three']

# Since variables one, two, and three in the mess_with_vars function are 
# local, reassigning them does not affect the original lists.

# 2nd func
def mess_with_vars(one, two, three):
    one = ["two"]
    two = ["three"]
    three = ["one"]

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")         # ["one"]
print(f"two is: {two}")         # ["two"]
print(f"three is: {three}")     # ["three"]

# Again, the local variables in the mess_with_vars function are being 
# reassigned, but this doesn't change the original lists.

# 3rd func
def mess_with_vars(one, two, three):
    one[0] = "two"
    two[0] = "three"
    three[0] = "one"

one = ["one"]
two = ["two"]
three = ["three"]

mess_with_vars(one, two, three)

print(f"one is: {one}")         # ["two"]
print(f"two is: {two}")         # ["three"]
print(f"three is: {three}")     # ["one"]

# In this case, the mess_with_vars function modifies the content of the lists 
# directly. Since lists in Python are mutable and passed by reference, the 
# changes are reflected outside the function.

# Question 4
# Ben was tasked to write a simple Python function to determine whether an 
# input string is an IP address using 4 dot-separated numbers, e.g., 10.4.5.11 

# Alyssa supplied Ben with a function named is_an_ip_number. It determines 
# whether a string is a numeric string between 0 and 255 as required for IP 
# numbers and asked Ben to use it. Here's the code that Ben wrote:

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False
    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

# Alyssa reviewed Ben's code and said, "It's a good start, but you missed a 
# few things. You're not returning a false condition, and you're not handling 
# the case when the input string has more or less than 4 components, e.g., 
# 4.5.5 or 1.2.3.4.5: both those values should be invalid."

# Help Ben fix his code. I nailed this exactly as per the solution!

# Question 5
# What do you expect to happen when the greeting variable is referenced in the 
# last line of the code below?

if False:
    greeting = "hello world"

print(greeting) # NameError: Undefined variable error