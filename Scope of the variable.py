"""
Here the scope is local
"""
x=10
def change_value_of_x(x):
    x=20

change_value_of_x(x)
print(x)


"""
Here the scope is global
"""
x=10

def change_value_of_x(x):
    x=20

x=change_value_of_x(x)
print(x)

"""
After return is done execution wont take place

"""
x=10

def change_value_of_x(x):
    x=20
    return x
    print("Hello")

x=change_value_of_x(x)
print(x)


"""
Function inside a function
"""

def fn2():
    print("This is fn2")
    def a():
        print("This is a")
    a()

fn2()