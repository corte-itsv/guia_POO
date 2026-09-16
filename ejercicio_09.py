class Temperature:
    def __init__(self, grados_celsius):
        self.grados_celsius = grados_celsius
    def to_fahrenheit(self):
        return self.grados_celsius * 1.8 + 32
    def to_kelvin(self):
        return self.grados_celsius + 273.15

t = Temperature(100)
print(f"Celsius: {t.grados_celsius}")
print(f"Fahrenheit: {t.to_fahrenheit()}")
print(f"Kelvin: {t.to_kelvin()}")