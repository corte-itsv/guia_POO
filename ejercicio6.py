class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"Insufficient funds. Current balance: {self.balance}")


account = BankAccount(1000)

account.deposit(500)
print(f"Balance after deposit: {account.balance}")

account.withdraw(200)
print(f"Balance after withdrawal: {account.balance}")

account.withdraw(2000)