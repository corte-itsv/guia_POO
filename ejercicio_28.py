class Character:
    def __init__(self, name, health, exp, level):
        self.name = name
        self.health = health
        self.exp = exp
        self.level = level
        
    def gain_exp(self, exp_gained):
        self.exp += exp_gained
        if self.exp >= 100:
            self.exp -= 100
            self.level += 1
            print(f"{self.name} gained {exp_gained} exp. Level up! Now Level {self.level}. (Remeaning exp: {self.exp})")
        else:  
            print(f"{self.name} gained {exp_gained} exp. (Total: {self.exp})")
        
c1 = Character("Aria", 100, 0, 1)


c1.gain_exp(60)
c1.gain_exp(60)
