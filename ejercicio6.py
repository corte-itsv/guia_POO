## Ejercicio 6: BankAccount con depósito y protección contra sobregiro

##**Pista:**
##- Inicializa `self.balance` en `__init__`.
##- En `deposit()`, suma el monto directamente a `self.balance`.
##- En `withdraw()`, usa una sentencia `if` para verificar si `amount <= self.balance` antes de descontar. Si no, imprime un mensaje de fondos insuficientes.

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


account = BankAccount(1000)
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)