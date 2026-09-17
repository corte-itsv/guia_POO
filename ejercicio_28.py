class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, xp):
        self.exp += xp
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} gained {xp}. Level up! Now level {self.level} exp (Remaining: {self.exp})")
        else:
            print(f"{self.name} gained {xp} exp (Total: {self.exp})")

c1=Character("Aria", health=100)
c1.gain_exp(60)
c1.gain_exp(60)