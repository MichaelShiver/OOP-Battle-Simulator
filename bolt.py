from spell import Spell

class Bolt(Spell):

    cost = 5
    damage = 5

    def __inti__(self):
        super().__init__(5, False, 5)
        self.cost = 5
        self.damage = 5

    