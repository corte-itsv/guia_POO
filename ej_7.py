class Light:
    def __init__(self, estado):
        self.estado = estado

    def turn_on(self):
        self.estado = "ON"
        print("Light is ON")

    def turn_off(self):
        self.estado = "OFF"
        print("Light is OFF")

    def status(self):     
        print(f"Current status: {self.estado}")

light = Light("OFF")

light.turn_on()
light.status()
light.turn_off()
light.status()
