
'''
Day 2 - Assignment
1. Declare an empty list
2. Read 5 numbers from users and save to the list
3. Traverse through all the numbers of that list and save even numbers to a separate list
4. Print the new list
'''

lst=[]
for n in range(0,5):
    lst[n]=int(input("Enter the number :"))

lst1=[]
i=0
for n in range(0,5):
    if(lst[n]%2==0):
        for i in range(0,5):
            lst1[i]=lst[n]
            i=i+1