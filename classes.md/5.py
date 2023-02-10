class Account:
     def __init__(self,owner,balance=0):
         self.owner = owner
         self.balance = balance
        
     def __str__(self):
         return f'Owner: {self.owner}  Account balance: {self.balance}$'
        
     def deposit(self,dep):
         self.balance += dep
         print('Deposit')
        
     def withdraw(self,wid):
         if self.balance >= wid:
             self.balance -= wid
             print('Withdraw')
         else:
             print('Not enough money')

acc = Account("Ayakoz", 100)
acc.deposit(100)
acc.withdraw(1000)
print(acc)