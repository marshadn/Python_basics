class Rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l*self.b
    
    def __lt__(self,other):
        return self.area() < other.area()
        
        
r1=Rectangle(2,5)
r2=Rectangle(3,8)

 

if r1 < r2:
    print("Area of r1 is less than r2")
    
else:
     print("Area of r2 is less than r1")    