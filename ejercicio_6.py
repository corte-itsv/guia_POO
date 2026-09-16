class BankAccount:
    def __init__(self,balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit: ", self.balance)
    

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds. Current balance: ",self.balance)
        else:
            self.balance -= amount
            print("Balance after withdrawal: ",self.balance)

if __name__ == "__main__":
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    account.withdraw(2000)
print()