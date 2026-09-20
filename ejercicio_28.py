class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, amount):
        self.exp += amount

        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} gained {amount} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
        else:
            print(f"{self.name} gained {amount} exp. (Total: {self.exp})")


character = Character("Aria", health=100)

character.gain_exp(60)
character.gain_exp(60)