class Temperature:
    def __init__(self, temperatura_C):
        self.temperatura = temperatura_C
        
    def to_fahrenheit(self):
        "(1 °C x 9/5) + 32 = 33,8 °F"
        temperatura_F = (self.temperatura * (9/5)) + 32
        return temperatura_F
    
    def to_kelvin(self):
        "1 °C + 273.15 = 274,15 K"
        temperatura_K = self.temperatura + 273.15
        return temperatura_K
    
t = Temperature(100)
print(f"Celsius: {t.temperatura}")
temp_F = t.to_fahrenheit()
print(f"Fahrenheit: {temp_F}")
temp_K = t.to_kelvin()
print(f"Kelvin: {temp_K}")