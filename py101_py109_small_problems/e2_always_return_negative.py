"""
Always Return Negative

Write a function that takes a number as an argument. 
If the argument is a positive number, return the negative of that number. 
If the argument is a negative number, return it as-is.
"""
def negative(num):
    print(-abs(num))          # Launch School solution to prefix the built-in abs() function with '-'
    return num if num < 1 else num - (num + num)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True