"""
open("filename","mode",)
"""

file=open("numbers.txt","r") # for reading numbers.txt in read mode

print(type(file))

print(dir(file)) # options that can be done

contents=file.read()
print(contents)


file.close() # Close each time 