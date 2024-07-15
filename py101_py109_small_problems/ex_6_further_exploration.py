"""
Further Exploration
Suppose the input was a list of space separated integers instead of just a single integer? How would your compute_sum and compute_product functions change?
"""

def compute_sum(target_num):
    return sum(range(1, target_num+1))

def compute_product(target_num):
    result = 1
    for num in range(1, target_num+1):
        result *= num
    return result

prompt1 = "Please enter an integer greater than 0: "
prompt2 = ('Enter "s" to compute the sum, '
           'or "p" to compute the product: ')

number = int(input(prompt1).replace(' ', ''))
operation = input(prompt2)
print()

if operation == "s":
    print("The sum of the integers between 1 and "
          f"{number} is {compute_sum(number)}.")
elif operation == "p":
    print("The product of the integers between 1 and "
          f"{number} is {compute_product(number)}.")
else:
    print("Oops. Unknown operation.")