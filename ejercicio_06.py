class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Balance after deposit: {self.balance}")
        return True
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Balance after withdrawal: {self.balance}")
            return True
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")
            return False
        
cuenta1 = BankAccount(1000)
cuenta1.deposit(500)
cuenta1.withdraw(200)
cuenta1.withdraw(2000)

# Balance after deposit: 1500
# Balance after withdrawal: 1300
# Insufficient funds. Current balance: 1300