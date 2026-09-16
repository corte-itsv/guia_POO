class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Balance after deposit: {self.balance}"


    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Balance after withdrawal: {self.balance}"
        else:
            return f"Insufficient funds. Current balance: {self.balance}"
account = BankAccount(1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.withdraw(2000))