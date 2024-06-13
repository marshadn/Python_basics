class Person:
    def __init__(self, name, age, mobile_number, address):
        self.name = name
        self.age = age
        self.mobile_number = mobile_number
        self.address = address

class Employee(Person):
    def __init__(self, name, age, mobile_number, address, salary):
        #Now we call the constructor of the base class i.e, Person
        super().__init__(name, age, mobile_number, address)
        self.salary = salary

    def print_details(self):
        print("---------------------------------------")
        print("----------------------")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Mobile Number:", self.mobile_number)
        print("Address:", self.address)
        print("Salary:", self.salary)
        print("---------------------------------------")
        print("----------------------")
# Input information
employee = Employee("Jhon", 28, "9546328791", "XYZ Street ,679023", 35000)
employee.print_details()
