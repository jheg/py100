# Even Numbers
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.

# Bonus Question: Can you solve the problem by iterating over just the even numbers?

# INPUTS / OUTPUTS
# Input:
# None
# Output: 
# odd numbers in 1 - 99

# EXAMPLE
# (1...99)
# 1
# 3   
# 5
# ...
# 99

def even_numbers():
    for num in range(2,99,2):
        print(num)

even_numbers()