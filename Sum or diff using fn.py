#Sum or Difference program using functions

def sum(x,y):
    return x+y

def diff(x,y):
    return x-y 

opera=input("Enter the operation to perform ie. sum or diff : (input sum or diff)")
x=int(input("Enter the first value: "))
y=int(input("Enter the second value: "))

if opera=="sum":                        # Where the sum of the values is to be taken
     print("The sum of the values is :",sum(x,y))
elif opera=="diff":                     # Where the data is to be made difference of   
     print("The difference of the values is :",diff(x,y))
else:                                   # Where the data is not valid
     print("Enter valid data")