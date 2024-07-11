# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# INPUT / OUTPUT
# inputs:
# None
# outputs: 
# odd numbers in 1-99

# EXAMPLE 
# 1
# 3
# 5
# 7
# ...

# Iterate through odd numbers in 1 to 99 and print each odd number on its own line.

def odd_numbers():
    for (num) in range(1,100, 2):
            print(num)

odd_numbers()


# Further Exploration
# Consider adding a way for the user to specify the starting and ending values of the odd numbers printed.

# INPUT / OUTPUT
# inputs:
# start number
# end number
# outputs: 
# odd numbers between the start number and end number

# EXAMPLE 
# (0,100)
# 1
# 3
# 5
# 7
# ...

# Iterate through odd numbers in the given range and print each odd number on its own line.

def my_odd_numbers(number1, number2):
    if number1 % 2 == 0:
        number1 += 1
    for (num) in range(number1, number2+1, 2):
        print(num)

print('0, 100')
my_odd_numbers(0,100)       # 1,3...99
print('1, 100')
my_odd_numbers(1,100)       # 1,3...99
print('0, 101')
my_odd_numbers(0,101)       # 1,3...101
print('1, 101')
my_odd_numbers(1,101)       # 1,3...101