areaSqure=lambda x:x*x

areaRectangle=lambda l,b:l*b

areaTriangle=lambda ba,h:(1/2)*ba*h

x=int(input("Enter the side of squre:"))
print("The area is",areaSqure(x))

l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("The area is",areaRectangle(l,b))


ba=int(input("Enter the base of triangle:"))
h=int(input("Enter the height of triangle:"))
print("The area is",areaTriangle(ba,h))