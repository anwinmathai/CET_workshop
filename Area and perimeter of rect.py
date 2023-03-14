"""
Area and Perimeter of a rectangle using functions for both.
Length and width are taken as input
"""


#Function to find the perimeter of the rectangle
def perimeter(l,w):
    return 2*(l+w)

#Function to find the area of the rectangle
def area(l,w):
    area_rectangle=l*w
    perimeter_rectangle=perimeter(l,w)
    return area_rectangle, perimeter_rectangle

#Getting the length and the width of the rectangle from the user
length=int(input("Enter the length of the rectangle :"))
width=int(input("Enter the width of the rectangle :"))

areaofrectangle,perimeterofrectangle=area(length,width)

print("Area of the Rectangle is :",areaofrectangle, "and perimeter of the Rectangle is :",perimeterofrectangle)