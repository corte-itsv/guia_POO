class Temperature:
    def __init__(self, temp):
        self.temp = temp

    def to_farenheit(self):
        return (32 + (self.temp*1.8))
    
    def to_kelvin(self):
        return (self.temp + 273.15)

t = Temperature(100)

print(f"Celsius: {t.temp}")
print(f"Farenheit: {t.to_farenheit()}")
print(f"Kelvin: {t.to_kelvin()}")