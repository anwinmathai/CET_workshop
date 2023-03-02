
'''
Sum the numbers present in the list and display it to the user
'''



a=int(input("Enter the number of numbers in the list :")) #Takes the number of elements the user wishes to input
lst=[] # Creates an empty list to get the numbers from the user
for n in range(0,a): #runs a loop a times
    lst.append(int(input("Enter the number to add to list: "))) #Appends the list to

sum=0
for n in range(0,a):
    sum=sum+lst[n]

print( "The sum is : ",sum)