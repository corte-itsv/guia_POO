class Light:
    def __init__(self):
        self.state = False
    
    def turn_on(self):
        self.state = True
        print(f"Light is ON")
        return self.state
    
    def turn_off(self):
        self.state = False
        print(f"Light is OFF")
        return self.state
    
    def status(self):
        if self.state == True:
            print(f"Current status: ON")
            return True
        else:
            print(f"Current status: OFF")
            
luz = Light()
luz.turn_on()
luz.status()
luz.turn_off()
luz.status()