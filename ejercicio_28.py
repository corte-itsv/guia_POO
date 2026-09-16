class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, sum):
        self.exp += sum
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} gained {sum} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
        else:
            print(f"{self.name} gained {sum} exp. (Total: {self.exp})")


per = Character("Aria", health=100)
per.gain_exp(60)
per.gain_exp(60)