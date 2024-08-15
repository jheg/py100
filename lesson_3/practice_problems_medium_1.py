from cmath import isclose
import math

# Question 1
# Let's do some "ASCII Art": a stone-age form of nerd artwork from back in the 
# days before computers had video screens.

# For this practice problem, write a program that outputs The Flintstones 
# Rock! 10 times, with each line prefixed by one more hyphen than the line 
# above it. The output should start out like this:

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#     ...

title = 'The Flintstones Rock!'
for num in range(1,11):
    print(f'{"-" * num}{title}')

# Question 2
# Alan wrote the following function, which was intended to return all of the 
# factors of number:

def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result

print(factors(5))

# Alyssa noticed that this code would fail when the input is a negative 
# number, and asked Alan to change the loop. How can he make this work? Note 
# that we're not looking to find the factors for negative numbers, but we want 
# to handle it gracefully instead of going into an infinite loop.

# Bonus Question: What is the purpose of number % divisor == 0 in that code?
# To determine if number / divisor is a factor, it is if the remainder is 0
# It determines whether the result of the division is an integer -- if the 
# number has no remainder, the result is an integer, so the number divided by 
# the divisor is a factor.


# Question 3
# Alyssa was asked to write an implementation of a rolling buffer. You can add 
# and remove elements from a rolling buffer. However, once the buffer becomes 
# full, any new elements will displace the oldest elements in the buffer.

# She wrote two implementations of the code for adding elements to the buffer:

def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)          # mutates original list
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]     # new list assigned to buffer
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer

# Is there a difference between these implementations, other than the way she 
# is adding an element to the buffer?
# Yes, there is a difference. The first function (add_to_rolling_buffer1) 
# mutates the original list represented by buffer. The second function 
# (add_to_rolling_buffer2) does not mutate the original list, but instead 
# creates a new list and assigns it to buffer, whose value ultimately gets 
# returned by the function.

# Question 4
# What will the following two lines of code output?

print(0.3 + 0.6)            # 0.8999999999999999
print(0.3 + 0.6 == 0.9)     # False

# If you thought that the outputs would be 0.9 and True, respectively, you 
# were wrong. Python uses floating point numbers for all numeric operations. 
# Most floating point representations used on computers lack a certain amount 
# of precision, and that can yield unexpected results like these.

# One way around the problem is to use the math.isclose function:
print(isclose(0.3 + 0.6, 0.9))

# Question 5
# What do you think the following code will output?

nan_value = float("nan")

print(nan_value == float("nan")) # False, python does not allow == to determine
# if a value is nan

# Bonus Question
# How can you reliably test if a value is nan?
print(math.isnan(float(nan_value)))


# Question 6
# What is the output of the following code?

answer = 42

def mess_with_it(some_number):
    return some_number + 8

new_answer = mess_with_it(answer)

print(answer - 8)

# 34

# Question 7
# One day, Spot was playing with the Munster family's home computer, and he 
# wrote a small program to mess with their demographic data:

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}

def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"

# After writing this function, he typed the following code:
mess_with_demographics(munsters)

# Before Grandpa could stop him, Spot hit the Enter key with his tail. Did 
# the family's data get ransacked? Why or why not?

# Spot will find himself in the "dog house" for this one. The family's data 
# is in shambles now. Dicts in python are mutable so when passed as the arg
# into the function the original is mutated.


# Question 8
# Function and method calls can take expressions as arguments. Suppose we 
# define a function named rps as follows, which follows the classic rules of 
# the rock-paper-scissors game, but with a slight twist: in the event of a 
# tie, it just returns the choice made by both players.

def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"

# What does the following code output?
print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

print(rps(
        rps( # paper
            rps("rock", "paper"), rps("rock", "scissors") # paper, rock
        ), 
        "rock"
        )
        )

# paper
# The outermost call determines the result of comparing rps(rps("rock", 
# "paper"), rps("rock", "scissors")) against rock. That means that we must 
# evaluate the two separate calls, rps("rock", "paper") and rps("rock", 
# "scissors"), and combine them by calling rps on their results. Those 
# innermost expressions return "paper" and "rock", respectively. Calling rps 
# on those two values returns "paper", which, when evaluated against "rock", 
# returns "paper".


# Question 9
# Consider these two simple functions:

def foo(param="no"):
    return "yes"

def bar(param="no"):
    return (param == "no") and (foo() or "no")

# What will the following function invocation return?
print(bar(foo()))

# False

# Question 10
# In Python, every object has a unique identifier that can be accessed using 
# the id() function. This function returns the identity of an object, which 
# is guaranteed to be unique for the object's lifetime. For certain basic 
# immutable data types like short strings or integers, Python might reuse the 
# memory address for objects with the same value. This is known as "interning".

# Given the following code, predict the output:

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))
# True
print(id(a))
print(id(b))
print(id(c))

# Here, a and c reference the same object in memory, so their ids are the 
# same. b will, in this case, have the same id as a and c due to interning. 
# Therefore, the code will output True.

# In Python, there's a predefined range of integers, specifically from -5 to 
# 256, for which memory locations are pre-assigned. When you reference an 
# integer within this span, Python consistently points to the same memory 
# spot. This strategy enhances efficiency since these particular numbers are 
# commonly utilized in many programming scenarios.

# However, when you work with integers outside of this specific range, Python 
# doesn't assure that it will consistently point to the same memory address 
# for identical values across different variables.

d = 257
e = 257
f = 0

print(id(d))
print(id(e))
print(id(f))







