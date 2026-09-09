class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 1.8) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

t = Temperature(100)
print("Celsius:", t.celsius)
print("Fahrenheit:", t.to_fahrenheit())
print("Kelvin:", t.to_kelvin())