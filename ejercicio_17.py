class employee:
    def __init__(self, name):
        self.name = name

    def calculate_pay(self):
        pass

class FullTimeEmployee(employee):
    def __init__(self, name, anual_salary):
        super().__init__(name)
        self.anual_salary = anual_salary

    def calculate_pay(self):
        return self.anual_salary / 12

class PartTimeEmployee(employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return self.hourly_rate * self.hours_worked

tiempo_comp = FullTimeEmployee("Alice", 60000)
medio_tiempo = PartTimeEmployee("Bob", 500, 20)

print(f"{tiempo_comp.name}'s monthly pay: {tiempo_comp.calculate_pay()}")
print(f"{medio_tiempo.name}'s monthly pay: {medio_tiempo.calculate_pay()}")