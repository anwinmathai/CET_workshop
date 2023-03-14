def perimeter(1,w):
    return 2*(1+w)

def area(1,w):
    area_rectangle=1*w
    perimeter_rectangle=perimeter(1,w)
    return area_rectangle, perimeter_rectangle

length=10
width=6

areaofrectangle,perimeterofrectangle=area(10,6)

print(areaofrectangle,perimeterofrectangle)