class Bank:
    def __init__(self,acc_no,acc_name,acc_type,balance):
        self.acc_no=acc_no
        self.acc_name=acc_name
        self.acc_type=acc_type
        self.balance=balance
        
        
    
    
    def deposit(self):
        balance=int(input("Enter the initial balnce:"))
        dep=int(input("Enter the amount to be deposit:"))
        newDep=balance+dep
        print(f"Current status is {newDep}")
        
    def withdarw(self):
        balance=int(input("Enter the the current balance:"))
        withd=int(input("Enter the amount to be withdraw:"))
        if withd>balance:
            print("You can't withdraw,Because you not have enough money")
        else:   
            newWithd=balance-withd
            print(f"Current status is {newWithd}")
            
    def details(self,acc_no,acc_name,acc_type,balance):
        return f"Acc.No:{self.acc_no}\n Acc.Name:{self.acc_name} \n Acc.Type:{self.acc_type}\n Balance:{self.balance}\n"
    
        
xyz=Bank(2323,'Fraz','Savings',0)
print(xyz.details(2323,'Fraz','Savings',0))
print(xyz.deposit())
print(xyz.withdarw())
       
        