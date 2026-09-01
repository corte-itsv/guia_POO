class CoffeeMachine:
    def __init__(self, water, coffee, milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk
    def make_latte(self):
        required_water = 200
        required_coffee = 20
        required_milk = 150

        if(
            self.water >= required_water and
            self.coffee >= required_coffee and
            self.milk >= required_milk
        ):
            self.water -= required_water
            self.coffee -= required_coffee
            self.milk -= required_milk
            print(
                f"Latte made! Remaining - Water: {self.water}ml, "
                f"Coffee: {self.coffee}g, Milk: {self.milk}ml"
            )
        else:
            print("Not enough resources to make a latte.")


machine = CoffeeMachine(300, 100, 200)

machine.make_latte()
machine.make_latte()