class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
        
    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            water_rest = self.water - 200
            coffe_rest = self.coffee - 20
            milk_rest = self.milk - 150
            
            print(f"Latte made! Reaming - Water: {water_rest}ml, Coffee: {coffe_rest}g, Milk: {milk_rest}ml")
        else:
            print(f"Not enough resources to make a latte.")

c1 = CoffeeMachine(water=300, coffee=100, milk=200)
c1.make_latte()