class Light:
    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print("Light is ON")

    def turn_off(self):
        self.is_on = False
        print(f"Light is OFF")

    def status(self):
        if self.is_on == True:
            print(f"Current status: ON")
        else:
            print(f"Current status: OFF")

light = Light()
light.turn_on()
light.status()
light.turn_off()
light.status()