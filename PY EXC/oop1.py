class Circle:
    def __init__(self,rad):
        self.rad=rad 
        
    def area(self,rad):
        return f"the area of the circle is {self.rad ** 2 *3.14}"
    
    def perim(self,rad):
        return f"primeter of circle is {2 * 3.14 * self.rad}"
    
    
r=Circle(int(input("Enter the radius:")))
print(r.area(r))
print(r.perim(r))