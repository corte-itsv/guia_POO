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

b1 = BankAccount(1000)
b1.deposit(500)
b1.withdraw(200)
b1.withdraw(2000)