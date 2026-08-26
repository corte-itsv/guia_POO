class Temperature:
    def __init__(self, celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return (self.celcius * 9/5) + 32 

    def to_kelvin(self):
        return self.celcius + 273.15

t = Temperature(100)
print("Celsius:", t.celcius)
print("Fahrenheit:", t.to_fahrenheit())
print("Kelvin:", t.to_kelvin())