from fighter import Fighter
from enemies import Goblin, Boss
from hero import Hero
from bolt import Bolt

ARENA_NAME = "The Jade Dodecagon"

def battle(hero: Hero, enemy : Fighter):
    while hero.is_alive() and enemy.is_alive():
        enemy.take_damage(hero.attack())
        print(f"{hero.name} Strikes {enemy.name}, who is left with {enemy.health} hp")
        if not enemy.is_alive():break
        hero.take_damage(enemy.attack())
        print(f"{enemy.name} Strikes {hero.name}, who is left with {hero.health} hp")

    if hero.is_alive():
        print(f"{hero.name} is victorious, with {hero.health} hp")
    else:
        print(f"{enemy.name} is victorious, with {enemy.health} hp")

def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    first_goblin = Goblin("Gribble")
    other_goblin = Goblin("Scribble")
    boss_goblin = Boss("Groglobno")

    print(f"{first_goblin.name} enters the arena with {first_goblin.health} health.")

    player = Hero("The Great Mage Apilacia")
    print(f"{player.name} enters the arena with {player.health} health.")
    battle(player, first_goblin)
    battle(player, other_goblin)



if __name__ == "__main__":
    main()
