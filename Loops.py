'''
To repeatedly run a process we use loops.

1. For loop

'''
for each_number in range(10):          #0 to 9 will come as output of range(10)
    print(each_number)


#Range : It has 3 parameters. range(start,stop,step)     step is by default 1

# To begin in 10 and end in 1
for each_number in range(10,0,-1):          #10 to1 will be the output of this
    print(each_number)


for n in range(3,33,3):     # increment by 3 and starts at 3 stops at 33-3
    print(n)


# Print each character in a string"
name="Gamer"
for n in name:
    print(n)

# Read a name, if upper case letter print it 

name=input("Enter the name: ")
for n in name:
    if n.isupper()==True:
        print(n)

''' While loop'''
#Perform a task as long as the condition is true
#Print numbers 0-10

number=0
while number<=10:
    print(number)
    number=number+1

# Program to print from 20 to 0 print 

number=20
while number> -1:
    print(number)
    number=number-1