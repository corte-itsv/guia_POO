class Employee:
    def __init__(self, name):
        self.name = name

class FullTimeEmployee(Employee):
    def __init__(self, name, yearly_salary):
        super().__init__(name)
        self.yearly_salary = yearly_salary

    def monthly_pay(self):
        return self.yearly_salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def monthly_pay(self):
        return self.hourly_rate * self.hours

full_time = FullTimeEmployee("Alice", 60000)
part_time = PartTimeEmployee("Bob", 500, 20)

print(f"{full_time.name}'s monthly pay: {full_time.monthly_pay()}")
print(f"{part_time.name}'s monthly pay: {part_time.monthly_pay()}")