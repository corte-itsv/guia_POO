class Temperature:
    def __init__(self, temp_celsius):
        self.temp_celsius = temp_celsius
        
    def to_farenheit(self):
        temp_fahrenheit = (self.temp_celsius * 9/5) + 32
        return temp_fahrenheit
    
    def to_kelvin(self):
        temp_kelvin = (self.temp_celsius + 273.15)
        return temp_kelvin
    
t = Temperature(100)
print(f"Celsius: {t.temp_celsius}")
print(f"Fahrenheit: {t.to_farenheit()}")
print(f"Kelvin: {t.to_kelvin()}")

        