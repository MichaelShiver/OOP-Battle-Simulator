class Spell:

    def __inti__(self, cost = None, is_ritual = None, damage = None):
        self.cost = cost
        self.is_ritual = is_ritual
        self.damage = damage

    def cast(self,target):
        target.take_damage(self.damage)