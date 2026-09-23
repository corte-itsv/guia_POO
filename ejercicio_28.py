class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.exp = 0
        self.level = 1
        
        
    def gain_exp(self, cant):
        if (self.exp + cant) >= 100:
            self.level += 1
            self.exp += cant
            self.exp -= 100
            return f"{self.name} gained {cant} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})"
        else: 
            self.exp += cant
            return f"{self.name} gained {cant} exp. (Total: {self.exp})" 
        
    
c1= Character("Aria", health=100)
print(c1.gain_exp(60))
print(c1.gain_exp(60))

