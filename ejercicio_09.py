class Temperature:
    def __init__(self, Celsius):
        self.celsius = Celsius

    def to_fahrenheit(self):
        fahrenheit = (self.celsius * 1.8) + 32
        return fahrenheit

    def to_kelvin(self):
        kelvin = self.celsius + 273.15
        return kelvin

t = Temperature(100)
print(f"Celsius: {t.celsius}")
print(f"Fahrenheit: {t.to_fahrenheit()}")
print(f"Kelvin: {t.to_kelvin()}")