#Develop a basic calculator hint: use if .. elif.. else
#1. Read two numbers from user
#2. Read an operation to do : Example "+" or "-"
#3. Check the operation and perform the corresponding operation
#4. Print the result

number1= int(input("Enter the first number:"))
number2= int(input("Enter the second number:"))

opera=input("Enter the operator:")
if opera=="+":
    print(number1+number2)
elif opera=="-":
    print(number1-number2)
elif opera=="*":
    print(number1*number2)
else:
    print(number1/number2)

