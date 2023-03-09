#Sum or Difference program using functions

def sum(x,y): #Sum function, has 2 arguments
    return x+y # Returns the sum

def diff(x,y): #Difference function, has 2 arguments
    return x-y  #Returns the difference 

opera=input("Enter the operation to perform ie. sum or diff : (input sum or diff)") # Takes in a string to know which function is to be performed
x=int(input("Enter the first value: ")) # Takes in the first input as integer
y=int(input("Enter the second value: ")) # Takes in the second input as integer

if opera=="sum":                        # Where the sum of the values is to be taken
     print("The sum of the values is :",sum(x,y))
elif opera=="diff":                     # Where the data is to be made difference of   
     print("The difference of the values is :",diff(x,y))
else:                                   # Where the data is not valid
     print("Enter valid data.")