class Publisher:
    def __init__(self,name):
        self.name=name
        
class Book(Publisher):
    def __init__(self,name,title,author):
        super().__init__(name)
        self.title=title
        self.author=author
        
    def info(self):
        print(f"Name:{self.name}")
        print(f"Title:{self.title}")
        print(f"Author:{self.author}")
class Python(Book):
    def __init__(self,name,title,author,price,no_pages):
        super().__init__(name,title,author)
        self.price=price
        self.no_pages=no_pages
        
    def info(self):
        super().info()
        print(f"Price:{self.price}")
        print(f"No.of Pages:{self.no_pages}")
        
result=Python("O Reially","Core Python","Marshad",350,400)
result.info()
    