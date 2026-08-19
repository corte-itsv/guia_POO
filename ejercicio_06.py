class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Balance after deposit: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Balance after withdrawal: {self.balance}")
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")

cuenta = BankAccount(1000)
cuenta.deposit(500)
cuenta.withdraw(200)
cuenta.withdraw(2000)