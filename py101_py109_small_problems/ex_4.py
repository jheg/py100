# How big is the room?

# Build a program that asks the user to enter the length and width of a room, 
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# INPUTS / OUTPUTS
# inputs: 
#  length
#  width
# output:
#  total area in square metres
#  total area in square feet

# EXAMPLE
# length:
#   10.3
# 
# width:
#   6.4 
# 
# area in square metres:
#   65.92
# 
# area in square feet
#   709.556288

# VALIDATION
# Example 1
# Inputs: 
#   Length:     10.0
#   Width:      10.0
# Outputs: 
#   100.0
#   1076.3899999999999


# MENTAL MODEL 
# Given two positive numbers, multiply them together to get a value. Then multiply the answer by a fixed number to get a second value. Return both values. 

# Create a variable called sq_metres and assign it the product of the two numbers 
# Create a variable called sq_feet and assign it the product of sq_metres and 10.7639
# Return sq_metres and sq_feet

length = float(input("What is the length of the room? "))
width = float(input("What is the width of the room? "))

def room_area(length, width):
    sq_metres = length * width
    sq_feet = sq_metres * 10.7639

    print(sq_metres)
    print(sq_feet)

room_area(length, width)


# Further Exploration
# Modify the program to let the user specify the measurement type (meters or feet). Compute the area accordingly and print it and its conversion in parentheses.

metric = input("Calculate the area of a room. Would you like to use metres or feet? ")
length = float(input(f"What is the total length im {metric}? "))
width = float(input(f"What is the total width im {metric}? "))

area = length * width

print(f"The area of the room is {area:.2f} square {metric}")