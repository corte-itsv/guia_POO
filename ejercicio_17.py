class Employee:
    def __init__(self, name):
        self.name=name
class FullTimeEmployee(Employee):
    def __init__(self, name, anual_pay):
        super().__init__(name)
        self.anual_pay=anual_pay
    def calculate(self):
        return self.anual_pay/12

class PartTimeEmployee(Employee):
    def __init__(self, name, day_pay, days):
        super().__init__(name)
        self.day_pay=day_pay
        self.days=days
    def calculate(self):
        return self.day_pay * self.days

e1=FullTimeEmployee("Alice", 60000)
e2=PartTimeEmployee("Bob", 500, 20)
print(f"{e1.name}'s monthly pay: {e1.calculate()}")
print(f"{e2.name}'s monthly pay: {e2.calculate()}")