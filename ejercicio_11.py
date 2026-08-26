class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk  = milk
        
    def make_latte(self, agua, cafe, leche):
        if agua <= self.water and cafe <= self.coffee and leche <= self.milk:
            self.water -= agua
            self.coffee -= cafe
            self.milk -= leche
            print(f"Latte made! Remaining - Water: {self.water}ml, Coffee: {self.coffee}g, Milk: {self.milk}ml")
            
        else:
            print("Not enough resources to make a latte.")
        
maquina = CoffeeMachine(water=300, coffee=100, milk=200)
maquina.make_latte(200, 20, 150)
maquina.make_latte(2000, 200, 1500)


        