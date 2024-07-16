"""
Odd Lists
Write a function that returns a list that contains every other element of a list that is passed in as an argument. 
The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.
"""
def oddities(arg):
    new_list = []
    for element in arg:
        if arg.index(element) % 2 == 0:
            new_list.append(element)

    return new_list

print(oddities([2, 3, 4, 5, 6]))
print(oddities([1, 2, 3, 4]))
print(oddities(["abc", "def"]))
print(oddities([123]))
print(oddities([]))


print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

"""
Really concise version.

def oddities(arg):
    return arg[::2]


Further Exploration
Write a companion function that returns the 2nd, 4th, 6th, and so on elements of a list.

Try to solve this differently from the exercise described above.
"""

def evens(lst):
    result = []
    for index in range(len(lst)):
        if index % 2 != 0:
            result.append(lst[index])
    
    return result

print(evens([2, 3, 4, 5, 6]))
print(evens([1, 2, 3, 4]))
print(evens(["abc", "def"]))
print(evens([123]))
print(evens([]))
