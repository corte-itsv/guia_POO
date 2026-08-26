class light:
    def __init__(self):
        self.estado = False

    def turn_on(self):
        self.estado = True
        print(f"light is ON")
    
    def turn_off(self):
        self.estado = False
        print(f"light is OFF")
    
    def status(self):
        if self.estado == True:
            print("current status: ON")
        elif self.estado == False:
            print("current status: OFF")

luz = light()
luz.turn_on()
luz.status()
luz.turn_off()
luz.status()