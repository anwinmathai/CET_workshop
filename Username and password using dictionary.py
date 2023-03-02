'''
We have a database called users to save the username and password as dictionary
'''
users={"Anwin":"nothin","Arvind":"hi","Athira":"054","Pearly": "8sfsd"}

username=input("Enter the username :")
if username in users:
    password=input("Enter the password: ")
    correctpassword=users[username]
    if password==correctpassword:
        print("It's right u can log in")
    else:
        print("SOrry")
