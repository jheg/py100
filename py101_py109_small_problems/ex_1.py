#  Isn't it odd?

# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

# INPUTS and OUTPUTS
#  input: 
#   target number
# output:
#   boolean

# EXAMPLE
# target number:
# 7
# False

# For a given number, determine if it is an even number or an odd number. Return True if the number is odd, otherwise return False

def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True

print(is_it_odd(3))             # True
print(is_it_odd(52))            # False
print(is_it_odd(2))             # False
print(is_it_odd(-1))            # True
print(is_it_odd(0))             # False

def better(num):
    return abs(num) % 2 == 1

print('------')
print(better(3.2))
print(better(52))
print(better(2))
print(better(-1))
print(better(0))

print(2 % 1)
print(2 % 5)
print(20 % 1)
print(7 % 13)

print('------')
print(2 % 1)
print(3 % 1)
print(20 % 1)
print(7 % 1)

print('------')
print(2 % 2)
print(3 % 2)
print(20 % 2)
print(7 % 2)
print('------')
print(-2 % 2)
print(-3 % 2)
print(-20 % 2)
print(-7 % 2)
print('------')
print(abs(2.3) % 2)
print(3.8 % 2)
print(20.2 % 2)
print(7.0 % 2)
print('------')
print(-2 % 1)
print(2 % 5)
print(20 % 1)
print(-7 % 13)          # 6
print(abs(-2) % 1)
print(abs(2) % 5)
print(abs(20) % 1)
print(abs(-7) % 13)     # 7