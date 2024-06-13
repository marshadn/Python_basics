

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) +fibo(n-2))

n=int(input("Enter the number:"))
fibo(n)
for i in range(n):
    print(fibo(i))








"""#This program print Fibonacci sequence #upto a given number
a, b = 1, 1
c=0
def fibernoci(n):
    if globals()['c'] == 0:
        if n>0:
            print(0)
    if n!=1:
        print(globals()['a'])
        globals()['a'], globals()['b'] = globals()['b'], globals()['a']+globals()['b']
        n-=1
        globals()['c']=1
        fibernoci(n)
    
n=int(input("Enter the number:"))
fibernoci(n)"""
