'''
Homework-3
Sign in
1. Take username and password 3 times
2. Add it to a dictionary
3. Use it to login and say if they can sign in

Also verify if they have already added and if they havent, allow sign in

'''

'''
Signup as well

'''

'''' Sign up'''
users={} #Database blank at first
print("...............Sign up...............")
j=int(input("Enter the number of users being taken in:"))
for n in range(0,j):
    username=input("Enter the username :") #Getting the username from the user
    if username not in users:
            users[username]=input("Enter the password for username :")
    else:
            print("Enter a valid username.")




'''           SiGN in                                                        '''
''' Sign in'''

print("...............Sign in.........................")
username=input("Enter the username:")
if username in users:             #Checking the password of the username by getting the password as well. 
    password=input("Enter the password: ")
    correctpassword=users[username]        #Correctpassword is present in the Database ie. dictionary
    if password==correctpassword:
        print("It's right. You are logged in.")
    else:
        print("Sorry,the password is wrong.")
