from fighter import Fighter

class Boss(Fighter):

    def __init__(self, name):
        super().__init__(name)
        self.health = 60
        self.attack_power = 30
        self.mana = 200
    
