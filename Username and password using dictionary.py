'''
We have a database called users to save the username and password as dictionary
'''
users={"Anwin":"nothin","Arvind":"hi","Athira":"054","Pearly": "8sfsd"} #Database

username=input("Enter the username :") #Getting the username from the user
if username in users:             #Checking the password of the username by getting the password as well. 
    password=input("Enter the password: ")
    correctpassword=users[username]        #Correctpassword is present in the Database ie. dictionary
    if password==correctpassword:
        print("It's right u can log in")
    else:
        print("SOrry,the password is wrong")
