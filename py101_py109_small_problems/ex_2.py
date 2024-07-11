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


