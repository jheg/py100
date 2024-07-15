# # Sum or Product of Consecutive Integers

# Write a program that asks the user to enter an integer greater than 0, 
# then asks whether the user wants to determine the sum or the product of 
# all numbers between 1 and the entered integer, inclusive.

"""
INPUT / OUTPUT
input: 
    target number
output: 
    sum or product of range from 1 to target number

target number:
5

sum of 1 to 5:
1+2+3+4+5

product of 1 to 5:
1*2*3*4*5

1. The input must be an integer greater than 0
"""

def sum_or_product():
    while True:
        target_number = int(input("Enter a whole number greater than 0: "))
        if target_number < 1:
            print("The number must be a whole number greater than 0.")
            continue
        break

    sum = 0
    product = 1
    for number in range(1,target_number+1):
        sum += number

    for number in range(1, target_number+1):
        product *= number

    while True: 
        choice = input("Do you want the sum (s) or the product (p) returned? ")
        if choice == "s".lower():
            break
        elif choice == "p".lower():
            break

        print("Please enter 's' or 'p'.")

    if choice == 's':
        print(f"The sum of the integers between 1 and {target_number} is {sum}.")
    else: 
        print(f"The product of the integers between 1 and {target_number} is {product}.")

sum_or_product()
