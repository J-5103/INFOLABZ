##function with no argument and no return

def func1():
    print("hello")

func1()

##function with argument and return

def func2(a,b):
    return a + b

print(func2(5,6))

##function with no argument and return

def func3():
    a = int(input("enter value of a:"))
    b = int(input("enter value of b:"))
    return a + b
print(func3())

##function with argument and no return

def func4(a,b):
    c = a + b
    print(c)

func4(5,6)