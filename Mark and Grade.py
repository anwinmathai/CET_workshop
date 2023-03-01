# Take mark from the user and help them know how to learn
mark=int(input("Enter your mark:"))
if mark >24:
    print("You have passed the test!")
    if mark>90:
        print("You have an A+.")
    elif 80>mark>90:
        print("You have an A.")
    else:
       print("Go and study!!") # Just an info
else:
    print("You failed")   #Failed