class Bank():
    _acc_no=""
    _acc_type=""
    _acc_name=""
    _acc_balance=0
    
    def __init__(self,acc_no,acc_type,acc_name,acc_balance):
        self._acc_no=acc_no
        self._acc_type=acc_type
        self._acc_name=acc_name
        self._acc_balance=acc_balance
        
    def deposit(self,deposit):
        print("Enter the Balance:",self.acc_balance)
        print("Enter the deposit",deposit)
        self._acc_balance+=deposit
        print("The accont balance is",self._acc_balance)
        
    def withdraw(self):
        print("Initial balance is",self._acc_balance)
        self.amount=int(input(("Enter the amount to be withdrawed:",self.amount)))
        
        if self.amount > self._acc_balance:
            print("You can't withdraw")
            
        else:
            print(self.amount,"is withdrawed")
            self._acc_balance-=self.amount
            print("The current balance is",self._acc_balance)
            
            
    def accInfo(ano,aty,anam,abal):
        print("Enter the acc.no:")
        print("Enter the acc.type:")
        print("Enter the acc.name:")
        print("Enter the acc.balance:")
        
    
            
        
    
    

        