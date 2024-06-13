class Person:
    def __init__(self, name, age, mobile_number, address):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.address = address

    def __str__(self):
        return f"Name: {self.name} Age:{self.age}"


person = Person("John", 28, "9546328791", "XYZ Street ,679023")
print(person)  
