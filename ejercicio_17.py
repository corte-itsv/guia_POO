class Employee:
    def __init__(self, name):
        self.name = name
    
class FullTimeEmployee(Employee):
    def __init__(self, name, yearly_pay):
        super().__init__(name)
        self.yearly_pay = yearly_pay
        
    def payment_logic(self):
        payment = self.yearly_pay / 12
        return payment
        
class PartTimeEmployee(Employee):
    def __init__(self, name, able_day_pay, able_days):
        super().__init__(name)
        self.able_day_pay = able_day_pay
        self.able_days = able_days
        
    def payment_logic(self):
        payment = self.able_day_pay * self.able_days
        return payment
        

p1 = FullTimeEmployee("Alice", 60000)
p2 = PartTimeEmployee("Bob", 500, 20)

print(f"{p1.name}´s monthly pay: {p1.payment_logic()}")
print(f"{p2.name}´s monthly pay: {p2.payment_logic()}")