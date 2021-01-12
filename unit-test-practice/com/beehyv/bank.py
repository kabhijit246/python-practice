class Bank:
    
    balance = 50000
    
#     def __init__(self, balance, depositAmount, withdrawlAmount):
#         self.balance = balance
#         self.depositAmount = depositAmount
#         self.withdrawlAmount = withdrawlAmount
        
    def checkBalance(self):
        print("Your current available balance is: Rs" + str(self.balance))
    
    def deposit(self, depositAmount):
        self.balance = self.balance + depositAmount
        print (f"You deposited Rs{depositAmount}")
        self.checkBalance()
    
    def withdrawl(self, withdrawlAmount):
        if(withdrawlAmount > self.balance):
            print("You don't have sufficient balance to withdraw, check your available balance.")
            
        else:
            self.balance = self.balance - withdrawlAmount
            print(f"You withdraw Rs{withdrawlAmount}")
            self.checkBalance()   
            
abhijit = Bank()
abhijit.checkBalance()   
abhijit.deposit(5000)
abhijit.withdrawl(6000)
abhijit.withdrawl(7000) 
abhijit.withdrawl(42000)  
abhijit.deposit(2000)
abhijit.deposit(6000)      
    