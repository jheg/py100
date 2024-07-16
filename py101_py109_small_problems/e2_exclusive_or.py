"""
Exclusive Or
The or operator returns a truthy value if either or both of its operands are truthy, 
a falsy value if both operands are falsy. The and operator returns a truthy value if 
both of its operands are truthy, and a falsy value if either operand is falsy. 
This works great until you need only one of two conditions to be truthy, the so-called exclusive or, 
also known as xor (pronounced "ECKS-or").

In this exercise, you will write an xor function that takes two arguments, 
and returns True if exactly one of its arguments is truthy, False otherwise.
"""

def xor(op1, op2):
    args = [op1, op2]
    count = 0
    for arg in args:
        if arg:
            count += 1

    return count == 1

print(xor(5, 0))
print(xor(False, True))
print(xor(1, 1))
print(xor(True, True))

"""
Other neat solution by Kevin Kang
def xor(op1, op2):
    return bool(op1) != bool(op2)
"""