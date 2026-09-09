class Light:
    def __init__(self,estado):
        self.estado=estado
    
    def turn_on(self):
        self.estado="ON"
        print(f"Light is {self.estado}")       

    def turn_off(self):
        self.estado="OFF"
        print(f"Light is {self.estado}")

    def status(self):
        print(f"Current status: {self.estado}")

luz=Light("OFF")
luz.turn_on()
luz.status()
luz.turn_off()
luz.status()