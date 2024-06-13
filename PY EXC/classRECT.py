class Rectangle:
    def __init__(self,l,b) :
        self.l=l
        self.b=b
        
    def area(self):
        return f"Area is {self.l*self.b}"
    
    
rect1=Rectangle(5,6)
rect2=Rectangle(10,5)

print(rect1.area())
print(rect2.area())

# if rect1.area(5,6)==rect2.area(4,7):
#     print("Both area are same")
    
# elif rect1.area(5,6) > rect2.area(4,7):
#         print("Area of rect 1 is graeter than rect 2")
        
# else :
#         print("Area of rect 2 is graeter than rect 1")

if rect1.area()==rect2.area():
    print("Both area are same")
    
elif rect1.area() > rect2.area():
        print("Area of rect 1 is  than rect 2")
        
else :
        print("Area of rect 2 is  than rect 1")