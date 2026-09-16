class Light:
    def __init__(self):
        self.is_on = False
    
    def turn_on(self):
        self.is_on = True
        print("The light is on.")

    def turn_off(self):
        self.is_on = False
        print("The light is off.")

    def status(self):
        state = "ON" if self.is_on else "OFF"
        print(f"The light is currently {state}.")

light = Light()
light.status()
light.turn_on()
light.status()
light.turn_off()
light.status()