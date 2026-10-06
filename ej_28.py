class Character:
    def __init__(self, nombre, health):
        self.nombre = nombre
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, xpganada):
        self.exp += xpganada
        if self.exp >= 100:
            self.level += 1     
            self.exp -= 100
            print(f"{self.nombre} gained {xpganada} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
        else:
            print(f"{self.nombre} gained {xpganada} exp. (Total: {self.exp})")


a = Character("Aria", 100)

a.gain_exp(60)
a.gain_exp(60)