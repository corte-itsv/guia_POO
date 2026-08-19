class CoffeeMachine:
	def __init__(self, water, coffee, milk):
		self.water = water
		self.coffee = coffee
		self.milk = milk

	def make_latte(self):
		water_needed = 200
		coffee_needed = 20
		milk_needed = 150

		if (
			self.water < water_needed
			or self.coffee < coffee_needed
			or self.milk < milk_needed
		):
			print("Not enough resources to make a latte.")
			return

		self.water -= water_needed
		self.coffee -= coffee_needed
		self.milk -= milk_needed
		print(
			f"Latte made! Remaining - Water: {self.water}ml, "
			f"Coffee: {self.coffee}g, Milk: {self.milk}ml"
		)


machine = CoffeeMachine(water=300, coffee=100, milk=200)
machine.make_latte()
machine.make_latte()