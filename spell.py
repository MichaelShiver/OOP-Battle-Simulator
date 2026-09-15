class Spell:

    def __inti__(self, 
             name,
             cost = 0,
             is_ritual = False,
        ):
        self.name = name
        self.cost = cost
        self.is_ritual = is_ritual
        self.damage = 0

    def cast(self,target):
        pass
