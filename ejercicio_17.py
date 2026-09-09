class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_pay(self):
        return 0



class FullTimeEmployee(Employee):
    def __init__(self, name, annual_salary):
        super().__init__(name)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return self.annual_salary / 12



class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked



ft = FullTimeEmployee("Alice", 60000)
pt = PartTimeEmployee("Bob", 500, 20)

print(f"{ft.name}'s monthly pay:{ft.calculate_pay()}")
print(f"{pt.name}'s monthly pay:{pt.calculate_pay()}")