# TODO: 1 import the Employee class from the employee module
from employee import Employee

# TODO: 2 create an empty list to store employees
employees = []

# TODO: 3 ask the user how many employees and store it in a variable n
n = int(input("How many employees do you want to add? :"))

# TODO: 4 write a loop that repeats n times
for i in range(n):
    print(f"\nEnter details for Employee {i + 1}:")
    name = input("Name: ")
    age = int(input("Age: "))
    mobile_number = input("Mobile Number: ")
    address = input("Address: ")
    salary = float(input("Salary: "))
    
    # TODO: 5 Inside the loop, ask the user for employee details and create an employee object.
    # also add the employee to the employees list(hint:use append method of list)
    employee = Employee(name, age, mobile_number, address, salary)
    employees.append(employee)

# TODO: 6 outside the loop, ask the user for a name
search_name = input("\nEnter a name to search for: ")

# TODO: 7 create another loop that iterates through the employees list, 
# and prints the details of employees with the given name
found = False
print("\nEmployee Details:")
for employee in employees:
    if employee.name == search_name:
        print("---------------------------------------")
        print("------------------------")
        print("Name:", employee.name)
        print("Age:", employee.age)
        print("Mobile Number:", employee.mobile_number)
        print("Address:", employee.address)
        print("Salary:", employee.salary)
        print("---------------------------------------")
        print("------------------------")
        found = True

# TODO: 8 if no employee with the given name is found, print "Employee not found"
if not found:
    print("Employee not found")
