class Light:
    def __init__(self, estado):
        self.estado = estado
        estado = "OFF"
    
    def turn_on(self):
        self.estado = "ON"
        return "Light is on"
    
    def turn_off(self):
        self.estado = "OFF"
        return "Light is off"
        
    
    def status(self):
        return self.estado
    
    
luz1 = Light("OFF")
print(luz1.turn_on())
print(f"Current status: {luz1.status()}")
print(luz1.turn_off())
print(f"Current status: {luz1.status()}")
    