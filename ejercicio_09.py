class Temperature:
    def __init__(self, Celsius):
        self.celsius = Celsius

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 1.8) + 32
        print(f"Fahrenheit: {fahrenheit}")

    def to_kelvin(self):
        kelvin = self.celsius + 273.15
        print(f"Kelvin: {kelvin}")

t = Temperature(100)
print(f"Celsius: {t.celsius}")
t.to_fahrenheit()
t.to_kelvin()