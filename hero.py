from fighter import Fighter
from spell import Spell
class Hero(Fighter):
    # TODO add more features to the hero, Special ablities?
    def __init__(self,name):
        super().__init__(name)

    def cast(self, spell : Spell, target : Fighter):
        print(f"{self.name} casts {spell.__name__} on {target.name} the {type(target).__name__}!")
        if self.mana >= spell.cost:
            spell.cast(spell, target)
        else:
            # TODO Implement a better return system
            raise ValueError("Cast a spell you have the Mana for")


    