m1=int(input("Enter the mark of student 1: "))
m2=int(input("Enter the mark of student 2: "))
m3=int(input("Enter the mark of student 3: "))
m4=int(input("Enter the mark of student 4: "))
m5=int(input("Enter the mark of student 5: "))
m6=int(input("Enter the mark of student 6: "))

markList=[m1,m2,m3,m4,m5,m6]
print(markList)
markList.sort()
print(f"The marks in sorted order is {markList}")
