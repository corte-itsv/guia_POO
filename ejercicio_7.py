class Light:
    def __init__(self):
        self.light = False

    def turn_on(self):
        if self.light == False:
            self.light = True 
            print("Light is ON")

        

    def turn_off(self):
        if self.light == True:
            self.light = False
            print("Light is OFF")


    def status(self):
        if self.light == False:
            print("Current status:OFF")
        else:
            print("Current status:ON")
         

if __name__ == "__main__":
    lamp = Light()
    lamp.turn_on()
    lamp.status()
    lamp.turn_off()
    lamp.status()



