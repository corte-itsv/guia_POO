
class Light:
    def __init__(self):
        self.encendida = False

    def turn_on(self):
        self.encendida = True
        print("Light is ON")

    def turn_off(self):
        self.encendida = False
        print("Light is OFF")

    def status(self):
        if self.encendida:
            print("Current status: ON")
        else:
            print("Current status: OFF")


luz = Light()

luz.turn_on()
luz.status()

luz.turn_off()
luz.status()