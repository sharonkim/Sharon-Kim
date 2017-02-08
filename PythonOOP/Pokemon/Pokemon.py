class Pokemon(object):
    def __init__(self, species = "Pikachu"):
        self._species = species
        self.moves = ["thunderbolt", "quick attack", "thunder", "double dash"]
        self.speed = 10
        self.hp = 10
        self.attack = 10
        self.defense = 10

    def say_name(self):
        return self._species

    def get_movement(self):
        return self.moves

    def set_name(self, name):
        self.name = name

pikachu = Pokemon()
print pikachu.get_name()
print pikachu.hp

class Pikachu(Pokemon):
    def __init__(self):
        super(Pikachu, self).__init__()
        self._species = "Pikachu"
        self.hp = 200

ralph = Pikachu()
print ralph.get_name()
print dir(ralph)

# poke2 = Pokemon()
# poke2.species = "Blastoise"
# print poke2.species

#fight
#color
#type1
#type2
#power
#walk
#personality
