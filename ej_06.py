class BankAccount:
    def __init__(self, balance):
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print(f"Balance after deposit: {self.balance}")

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance-=amount
            print(f"Balance after withdrawal: {self.balance}")
        else:
            print(f"Insuficient funds. Current Balance: {self.balance} ")

cuenta1=BankAccount(1000)
cuenta1.deposit(500)
cuenta1.withdraw(200)
cuenta1.withdraw(2000)