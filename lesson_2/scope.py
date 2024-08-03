# Ex 1
num = 5

def my_func():
    print(num)

my_func()       # Will print 5 as my_func can access vars in the globalscope

# Ex 2
num_ex2 = 5

def my_func2():
    num_ex2 = 10

my_func()
print(num_ex2)  # Will print 5. The function call cannot mutate vars in the 
                # global scope. 

# Ex 3
num_ex3 = 5

def my_func3():
    global num_ex3
    num_ex3 = 10

my_func3()
print(num_ex3)  # Will print 10. The global keyword tells the function to 
                # use the global var which gives it access to mutate it. 

# Ex 4
def outer():
    outer_var = "Hello"

    def inner():
        inner_var = "World"
        print(inner_var, outer_var)

    inner()

outer()         # Will print "Hello World" as inner() has access to 
                # ascendent variables as well as global

# Ex 5
def my_func5():
    num = 10

my_func5()
print(num)      # Will raise a NameError as num not defined error

# Ex 6
def my_func6():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()               # "Inner 1: 25"
    inner_func2()               # "Inner 2: 15"

my_func6()