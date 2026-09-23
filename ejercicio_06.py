class BankAccount:
    def __init__(self, balance):
        self.balance = balance
        
    def deposit(self, amount):
        if amount > 1:
            self.balance += amount
        else:
            return "Monto inválido"
        
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            return "Saldo insuficiente"
        
p1 = BankAccount(1000)
p1.deposit(500)
print(f"Balance after deposit: {p1.balance}")
p1.withdraw(200)
print(f"Balance after withdrawal: {p1.balance}")
print(f"{p1.withdraw(2000)}. Current balance: {p1.balance}")

