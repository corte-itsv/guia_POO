class light:
    def __init__(self):
        self.estado = False

    def turn_on(self):
        self.estado = True
        print(f"Light is ON")
    
    def turn_off(self):
        self.estado = False
        print(f"Light is OFF")
    
    def status(self):
        if self.estado == True:
            print("Current status: ON")
        elif self.estado == False:
            print("Current status: OFF")

luz = light()
luz.turn_on()
luz.status()
luz.turn_off()
luz.status()