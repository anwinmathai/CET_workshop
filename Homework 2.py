
'''
Day 2 - Assignment
1. Declare an empty list
2. Read 5 numbers from users and save to the list
3. Traverse through all the numbers of that list and save even numbers to a separate list
4. Print the new list
'''

lst=[] #an empty list to take in all the 5 numbers
for n in range(0,5): #there will be 5 values of n from 0 onwards working as index
    lst.append(int(input("Enter the number :")))

print(lst)

lst1=[] #making an empty list for saving the even numbers

for n in range(0,5):
    if(lst[n]%2==0):
        lst1.append(lst[n])
            
print("The even numbers in the list are",lst1) #lst1 is the list of even numbers