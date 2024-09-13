# Specific Topics of Interest

## Some terms to remember
Expressions
- 2 + 5                           # 
- myvar1 += 1                     # arythmic operations
- print('Hello') or len('Python') # function calls
- 3.141592
- True

An expressions is something that has a value

Statements
Statements are instructions that tell python to perform an action of some kind.
Statements do not return a value like expressions do. 

For example, 
- return myvar
- def and class
- myvar = 5
- if, else, while, for and so on
- import

Expressions return a value; statements do not. 

In the following code a = is a statement and b + c is an expression. 
```python
a = b + c
```

Some grey areas are whereby an expression is standalone. They are not part of 
a statement and their return values are ignored. These can be considered both 
an expression and a statement. Some examples:

```python
2 + 4                   # Simple expression
print('Hello world')    # function call; returns None 
my_list.sort()          # method call; returns None
```

### initialising, assignement and reassignment
'''python
myvar = 10
myvar = 12
'''
In the code above a variable is created called myvar and then assigned a value
of 10. myvar is then reassigned to a value of 12.

myvar was inititalised with a value of 10.

## naming conventions: legal vs. idiomatic, illegal vs. non-idiomatic

Non-idiomatic versus illegal. 

Illegal variable names:
- Start with a numeric
- Use a reserved word such as if, def, range
- Include hyphens '-'
- Contain whitespace
- Use special characters like +, / or *
- Use punctuation

Non-idiomatic names: 
- Extended ASCII characters 
- camelCase variable names

The following is legal but idiomatic:
myVar = 10

This is both legal and idiomatic
my_var = 10

## type coercions: explicit (e.g., using int(), str()) and implicit

Type coercion occurs when you want to coerce a value from one type to another, 
for example str to int.

```python
print(int('1'))     # 1
print(float('1'))   # 1.0
```

The int() function takes a string and attempts to coerce is to an integer
The float() function takes a string and attempts to coerce it to a float

You can also coerce a numeric value to a string value. Python can coerce most
python values to strings. 

```python
print(str(1.0))     # 1.0
```

Implicit and Explicit coercion
The examples above are sometimes referred to as explicit coercion but python 
also has implicit coercion. Implicit coercion can be handy as the are more 
readable and save typing.

The print() function will implicitly coerce the object to a string before 
printing it.

```python
print(1.0)          # 1.0
```

Implicit coercion also occurs when mixing numbers of different types:

int float = float
int Decimal = Decimal
int Fraction = Fraction
float Decimal = --error--
float Fraction = float
Decimal Fraction = --error--

Gotchas may occur unexpectidly when using booleans in an arythmitic expression.

True + 1 = int
True * 2000 = float

## boolean vs. truthiness
Many languages can evaluate objects and values as either truthy or falsy. 
Python can too. These are terms to describe how these behave in a Boolean 
context. 

Truthiness arrises in conditional expressions such as if and while statements.

For example, myvar1 here is assigned to a truthy value of 10 whereas myvar2
evaluates as a falsy value:

```python
myvar1 = 10
myvar2 = 0

if myvar1:
    print(True)
else: 
    print(False)

# True

if myvar2:
    print(True)
else: 
    print(False)

# False
```

## None 
None is a literal whose value is the sole representitive of the NoneType class. 

## Sequences (and Text sequences)
The following are sequences 
- Strings although unlike other sequences they do not contain ojects
- lists
- tuples
- range

## list and dictionary syntax
Strings, lists, tuples and ranges all support index access to individual 
elements in the collection. When trying to access an index out of the 
collections range you will get an IndexError.

Examples: 
```python
my_string = '12345'
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_range = range(1,5)

print(my_string[2])     # 3
print(my_list[2])       # 3
print(my_tuple[2])      # 3
print(my_range[2])      # 3
print(my_list[5])     # IndexError: list index out of range
```

Dictionaries use keys to access items in a dictionary. Like indexes you will 
get an error if the key does not exist.

Examples: 
```python
my_dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
}

print(my_dict['3'])     # 3
```

Since lists and dictionaries ar emutable you can use [] to access 
replace elements in the collections. Unlike lists though, you can also use [] 
to create new items in dictionaries. 

Note that strings, ranges, tuples, and frozen sets are immutable, so they do 
not support using [] for updates. Sets are mutable, but they don't support 
indexing.

```python
my_list = [1, 2, 3, 4, 5]

my_list[2] = 9
print(my_list)                  # [1,2,9,4,5]
my_list[5] = 'new element'      # IndexError: list assignement out of range

my_dict = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,   
}
my_dict['3'] = 9
print(my_dict)          # {'1': 1, '2': 2, '3': 9, '4': 4, '5': 5}
my_dict['6'] = 6
print(my_dict)          # {'1': 1, '2': 2, '3': 9, '4': 4, '5': 5, '6': 6}
```
This code demonstrates how you can replace elements in both lists and 
dictionairies but only dictionaries allow you to use [] to create new items. 

## list methods: len(list), list.append(), list.pop(), list.reverse()
len(list) returns an integer count equal to the number of elements in the list
list.append() adds an elment to the end of list. 
list.pop() removes and returns the last element in the list. If an index is 
given then it will remove and return the element at the given index.
list.reverse() mutates list by reversing the order of elements in the 
collection

## dictionary methods: dict.keys(), dict.values(), dict.items(), dict.get()
dict.keys() returns a list of keys wrapped in dictionary view
dict.values() returns a list of values wrapped in dictionary view
dict.items() returns a list of items wrapped in dictionary view
dict.get() returns the value at associated to the key passed as the argument

## slicing (strings, lists, tuples)
The indexing syntax also supports a slicing augmentation. The syntax is as 
follows: seq[start:stop:step]

In the following code 

```python
address = '10 The Street, The Town, The County, IP10 1IP'
print(address[0:16])        # 10 The Street, T
print(address)              # 10 The Street, The Town, The County, IP10 1IP
```
The first print function prints characters from index 0 to 16 of the value 
assigned to address. The second print function prints the entire value assigned
to address.

## operators

list operators: +
The + operator allows you to add and return two or more other lists together. 

## variables as pointers
Note: Pointers are often referred to be devs as references.
You can say a variable points to or references an object in memory. You can 
also say the pointers stored in variables are references. Some languages make 
a distinction betwen the two, Python does not.


In the following code example, we create a variable called numbers and assign 
a list of numbers from 1 to 5. We then 'mutate' the list by replacing the element at index 2 with 999.

This is not reassignment of the numbers variable although it is reassignment of the element at index 2. 

```python
numbers = [1, 2, 3, 4, 5]
numbers[2] = 999
```

It's important to remember that some operations mutate objects while others do not. For example list.sort mutates a list but sorted(list) does not. 

At a basic level variables are named locations in a computers memory. Each has a unique address in memory usually in an area called the stack and sometimes im a different area called the heap.

### Variables and Objects
When you create a new variable Python adds a new entry into the stack. The space allocated for this is small, typically 8 bytes (64 bits). Objects do not usually get stored on the stack as they often exceed that size. Python allocates the space the object from the heap. Assuming there is sufficient space Heap blocks can be any size.

Once the space is allocated it creates and stores the object at that location. The address of that object is tehn copied to the variables stack location.

So when you access a variable, Python first goes to the variables address in the stack, gets the object address and then retrieves it from the Heap.

The variable is a pointer to the stack location and the stack location is a pointer to the object.

### Shallow vs Deep Copies
import copy

list1 = [1, 2, 3, [4, 5]]
list2 = list1[::-1]
list3 = copy.copy(list1)
list4 = copy.deepcopy(list1)

print(list1[3] is list2[3]) # False

print(list1[3] is list3[3]) 

print(list1[3] is list4[3])
print(id(list1))
print(id(list2))
print(id(list3))
print(id(list4))

# What does this print and why? What concept does this cover?
# Pass by object reference
# variables as pointers

# copy.copy(obj)
# copy(obj)

## variable shadowing

