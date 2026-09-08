class Vehicle:
    def __init__(self,modelo,max_speed,mileage):
        self.modelo = modelo
        self.max_speed = max_speed
        self.mileage = mileage
    def __str__(self):
        return "Vehicle Name:" + self.modelo + " Speed:" + str(self.max_speed) + " Mileage:" + str(self.mileage)



if __name__ == "__main__":
    vehicle1 = Vehicle("Tesla Model S", 250, 18)
    print(vehicle1)
