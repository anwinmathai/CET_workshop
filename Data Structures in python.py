''' Data structures in python'''

''' Data structures are formats to store and organize data efficiency'''

# 1. List

 #comma separated any type data in between []
 #List is an ordered datastructure, so we can use the index
list_a=[1,2,3,4,10]

list_b=[]
list_b.append(10)
print(list_b)


# get 3 numbers from user in a list named Gamers
Gamers=[]
for n in range(1,4):
    Gamers.append(input("Enter the Gamer:"))

print(Gamers)


# Accessing string elements
string="Python"
print(string[2]) # Gives t as output

#Access elements in list as per the index
stri="asdfahahzrfdsg"
for n in range(2,5):
    print(stri[n])


a=[1,2,4,9]
element=0
for element in a:
    print(a[element])

#we can change the list elements ie. mutable
a[2]=20
print(a)

''' List slicing '''

mylist=[1,2,3,6,9]
print(mylist[0:3]) # Show 0th to 2nd index of mylist

a="python"
print(a[0:3]) # similar slicing can be done in strings

''' 2. Tuple
Also an ordered datatype like list.
Immutable dataset. So constants are saved here.

'''
a=(1,2,3) #In the paranthesis
print(a[1]) #print 2

'''
3. Dictionary
Used to save key:value pair
any datatype can be used as key.
'''
marks={"Radha":60, "Krishna":5} # Key comes first, then value.

#if we want to find the mark of a corresponding key lets say Radha
print(marks["Radha"])