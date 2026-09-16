class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_pay():
        return 0

class FullTimeEmployee(Employee):
    def __init__(self, name, anual_salary ):
        super().__init__(name)
        self.anual_salary = anual_salary

    def salary(self):
        return self.anual_salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

full_time =FullTimeEmployee("Alice", 60000)
part_time =PartTimeEmployee("Bob", 500, 20)

print(f"{full_time.name}'s monthly pay: {full_time.calculate_pay()}")
print(f"{part_time.name}'s monthly pay: {part_time.calculate_pay()}")

