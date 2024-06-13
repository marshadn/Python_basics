# it stores the information about a student
student={
    "name":"Marshad",
    "age":22,
    "course":"Django Malayalam Course"
         }
# print(student)
# # adding a new key-value pair 'grade' to the dictionary
# student["grade"]=100
# # print the updated dictionary
# print(student)

# we can also add a new data to the dictionary by using update fn
student.update({"grade":100}) 

print(student)