from goblin import Goblin


ARENA_NAME = "The Jade Dodecagon"


def main():
    """Open the arena and introduce its first opponent."""
    print(f"Welcome to {ARENA_NAME}!")
    print("༼ ᓄºل͟º ༽ᓄ   ᕦ(ò_óˇ)ᕤ")
    print("The gates are opening...")

    goblin = Goblin("Gribble")
    other_goblin = Goblin("Scribble")

    print(f"{goblin.name} enters the arena with {goblin.health} health.")
    print(f"{other_goblin.name} enters the arena with {other_goblin.health} health.")
    print("But no hero has answered the call... yet.")


if __name__ == "__main__":
    main()
