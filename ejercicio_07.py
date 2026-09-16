class Light:
    def __init__(self):
        self.prendido = False
    def turn_on(self):
        self.prendido = True
        print("Light is ON")
    def turn_off(self):
        self.prendido = False
        print("Light is OFF")
    def status(self):
        if self.prendido == True:
            estado = "ON"
        else:
            estado = "OFF"
        print(f"Current status: {estado}")

Light1 = Light()
Light1.turn_on()
Light1.status()
Light1.turn_off()
Light1.status()

