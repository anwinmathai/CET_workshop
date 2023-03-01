#If-elseif

mark=81 #Hardcode

if mark>90:
    print("You have an A+")
elif mark>80 and mark<90:
    print("You have A grade")
else:
    print("You don't have A+ or A grade.")


#Softcoding
mark=int(input("Enter your mark please: "))

if mark>90:
    print("You have an A+")
elif mark>80 and mark<90:
    print("You have A grade")
else:
    print("You don't have A+ or A grade.")