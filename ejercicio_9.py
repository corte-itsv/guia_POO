class Temperature:
    def __init__(self,celcius):
        self.celcius = celcius

    def to_fahrenheit(self):
        return self.celcius * 9/5 + 32

    def to_kelvin(self):
        return self.celcius + 273.15

if __name__ == "__main__":
    t = Temperature(100)
    print(t.celcius)
    print(t.to_fahrenheit())
    print(t.to_kelvin())