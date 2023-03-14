"""
Print the even numbers in the file named 
"""
file=open("random.txt","r") # for reading numbers.txt in read mode and text is read.

print(type(file)) #to know what type of data is read and saved in file. its <class '_io.TextIOWrapper'>


file.close()
"""
This is a wrong method as a two digit at final line will be considered as only one digit

contents=file.read() #Not used as we are going to read lines and make it an array
for content in contents:
    if content.isdigit():
        if int(content)%2==0:
            print(content)

"""
#1
#.strip() removes spaces or \n characters in the string
file=open("random.txt","r") 
contents=file.readlines() #Makes a list of the characters
for element in contents:   #loop through the content text
    if int(element.strip())%2==0:  #strips off \n and white spaces and converts the text to integer
        print(element.strip())




file.close() # Close each time it is open


#2
#Comma separated numbers in the file random2.txt
file=open("random2.txt","r") 
contents=file.read() #read directly then only use split. We can only split the line. not list.
contents=contents.split(",") # As per which character the split is to be done.
print(contents) #To print the content which was split using the split function

for element in contents:   #loop through the content text
    if int(element.strip())%2==0:  #strips off \n and white spaces and converts the text to integer
        print(element.strip())
file.close()


#3. "w" mode ie. write mode
# To write something to a file if its even
# By default python makes a file, else it will delete the file already present.
file_to_read = open("numbers.txt")
file_to_write= open("evens.txt","w")
for num in contents:
    if int(num) %2==0:
        #Write the number to a different file
        file_to_write.write(num)
        file_to_write.write("\n") # To write in the next line
        print(num)
file.close()


#4. "a" mode ie. append mode

file_to_read = open('numbers.txt')
file_to_write= open("evens.txt","a")
for num in contents:
    if int(num) %2==0:
        #Write the number to a different file
        file_to_write.write(num)
        file_to_write.write("\n") # To write in the next line
        print(num)
file.close()




#5. with open()
# Automatically closes the file 
with open("evens.txt","r") as file:
    print(file.read())

#6 with open to do write
# Automatically closes the file
with open("evens.txt","a") as file:
    print(file.write("End"))
 #Going to check if its there
with open("evens.txt","r") as file:
    print(file.read())
    