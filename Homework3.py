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
users={} #Database

for n in range(0,3):
    username=input("Enter the username :") #Getting the username from the user
    if username!=users.keys():
            users[username]=input("Enter the password for username :")
    else:
            print("Enter a valid username.")
