from fighter import Fighter

class Goblin(Fighter):
 # The basic enemy, fairly weak, ut stronger in groups

    def __init__(self, name):
        super().__init__(name)
        self.health = 50
        self.attack_power = 10


