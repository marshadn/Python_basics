
def leapyr(year):
    if (year % 4 == 0 and year%100!=0) or (year%400==0):
        return f"it's a leap year"
    
    else:
        return f"its not a leap year"
    
x=int(input("Enter the year:"))
y=leapyr(x)
print(y)