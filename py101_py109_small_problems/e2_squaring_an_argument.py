"""
Squaring an Argument
Using the multiply function from the "Multiplying Two Numbers" exercise, 
write a function that computes the square of its argument (the square is the result of multiplying a number by itself).
"""

def multiply(n1, n2):
    return n1 * n2

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True

"""
Further Exploration
Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. 
How would we go about doing so while still using the multiply function?

=> Ask for inputs to get two numbers and assign to variables
=> Begin calling the multiply function as many times as is needed
=> Pass in the number_to_multiply and to_the_power to the multiply function
=> Update the value of number_to_multiply with the returned value
=> Repeat until every number in to_the_power has been run
=> Return number_to_multiply

==> 5 * 5 * 5 * 5 * 5 = 3125
"""

def power_of():
    number_to_multiply = int(input('Enter the number you want to multiply: '))
    to_the_power = int(input('Enter the number you wish to multiply by: '))
    total = number_to_multiply

    for n in range(1, to_the_power):
        total = multiply(total, number_to_multiply)

    return total

print(power_of())