"""
Functions are for
----------------------
For reusability of code
"""

"""
Structure
-----------
def name():
    statement1
    statement2
"""

#Example 1: without argument, without return
def display_message():
    print("Hello Mahn!")
    return None #This is not a compulsory line, by default if not given then None is returned

display_message()

#Example 2: With argument no return
def display_message(sdf):
    print(sdf)

x=input("Enter the stuff to print: ")
display_message(x)

#Example 3: With argument With return

def add(y,x):
    return x+y

result=add(10,5)
print(result)

