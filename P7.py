class BankAccount:
    def __init__(self,balance=1000):
     self.balance= balance
    
    
    def deposit(self,balance):
        self.balance += balance
        return self.balance

    def withdraw(self, balance):
        if balance > self.balance:

            raise ValueError(f"Cannot withdraw {balance}, balance is {self.balance}")
        self.balance -= balance
        return self.balance


A = BankAccount()
print("Balance after Cashdeposit:", A.deposit(500))
print("Balance after CashWithdrawan:", A.withdraw(300) )
try:
    print("Balance ater withdrawl:", A.withdraw(5000))
except ValueError as e:
    print(e)
        