class temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return(self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

t = temperature(100)
print(f"celsius: {t.celsius}")
print(f"fahrenheit:{t.to_fahrenheit()}")
print(f"kelvin: {t.to_kelvin()}")