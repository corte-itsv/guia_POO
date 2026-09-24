class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print("Light is OFF")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"Current status: {state}")


light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()