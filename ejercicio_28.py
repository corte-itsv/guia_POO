class Character:
    def __init__(self, nombre, health):
        self.nombre = nombre
        self.health = health
        self.exp = 0
        self.level = 1

    def gain_exp(self, cantidad):
        self.exp += cantidad

        if self.exp >= 100:
            self.level += 1
            self.exp -= 100
            return f'{self.nombre} gano {cantidad} exp. nivel {self.level}. (lo que queda {self.exp})'
        else:
            return f'{self.nombre} gano {cantidad} exp. (Total: {self.exp})'


aria = Character("Aria", health=100)

print(aria.gain_exp(60))
print(aria.gain_exp(60))