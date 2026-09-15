from spell import Spell

class Bolt(Spell):

    cost = 5
    damage = 5

    def __inti__(self):
        super().__init__("Bolt", 5, False)
        self.cost = 5
        self.damage = 5

    