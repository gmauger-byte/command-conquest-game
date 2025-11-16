#simple text-based adventure game named "Comand Conquest"

import random

print("Welcome to Comand Conquest!")
print("Create a character and embark on an epic journey.")

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.score = 0

class Stats:
    def __init__(self, player):
        self.player = player

    def show_stats(self):
        self.player.constitution = 10
        self.player.strength = 10
        self.player.dexterity = 10
        self.player.intelligence = 10
        print(f"Stats for {self.player.name}:")
        print(f"Constitution: {self.player.constitution}")
        print(f"Strength: {self.player.strength}")
        print(f"Dexterity: {self.player.dexterity}")
        print(f"Intelligence: {self.player.intelligence}")

class Skills:
    def __init__(self, player):
        self.player = player

    def show_skills(self):
        self.player.swordsmanship = 5
        self.player.archery = 5
        self.player.magic = 5
        print(f"Skills for {self.player.name}:")
        print(f"Swordsmanship: {self.player.swordsmanship}")
        print(f"Archery: {self.player.archery}")
        print(f"Magic: {self.player.magic}")

player_name = input("Enter your name, adventurer: ")
player = Player(player_name)
print(f"Welcome, {player.name}! Your journey begins...")

class Inventory:
    def __init__(self, player):
        self.player = player

    def add_item(self, item):
        self.player.inventory.append(item)
        print(f"{item} has been added to your inventory.")

    def show_inventory(self):
        if self.player.inventory:
            print("Your inventory contains:")
            for item in self.player.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

def show_status():
    print(f"Health: {player.health}")
    print(f"Score: {player.score}")
    Inventory(player).show_inventory()

def explore():
    print("You walk into a dark forest.")
    print("A wild creature appears!")
    action = input("Do you [fight] or [run]? ")
    if action.lower() == "fight":
        print("You bravely fight and win!")
        player.score += 10
        show_status()
        Inventory(player).add_item("Zephyr Blade")
        player.health -= 10
        show_status()
    elif action.lower() == "run":
        print("You escape safely, but miss out on treasure.")
        player.score -= 5
        show_status()
    else:
        print("You hesitate and the creature vanishes.")
        player.score -= 2
    show_status()

def rest():
    print("You find a safe spot to rest.")
    player.health += 20
    if player.health > 100:
        player.health = 100
    print("You feel rejuvenated.")
    show_status()

def level_up():
    print("Congratulations! You've leveled up!")
    player.score += 20
    player.health += 10
    if player.health > 100:
        player.health = 100
    show_status()
    level_up()


def village():
    print("You arrive at a peaceful village.")
    print("Villagers offer you food and shelter.")
    rest()
    Inventory(player).add_item("Village Token")

def cave():
    print("You enter a dark cave.")
    print("You find hidden treasures!")
    if player.dexterity > 8:
        print("You deftly avoid traps and find a hidden stash!")
    Inventory(player).add_item("Ancient Amulet")
    player.score += 15
    show_status()

def abandoned_castle():
    print("You explore an abandoned castle.")
    print("Ghostly figures appear!")
    action = input("Do you [confront] or [flee]? ")
    if action.lower() == "confront":
        print("You bravely confront the ghosts and earn their respect!")
        player.score += 20
        show_status()
    elif action.lower() == "flee":
        print("You escape, but feel a chill down your spine.")
        player.score -= 10
        show_status()
    else:
        print("You stand frozen as the ghosts disappear.")
        player.score -= 5
    show_status()

def random_encounter():
    encounters = ["monster", "treasure", "ally", "nothing"]
    encounter = random.choice(encounters)
    if encounter == "monster":
        print("A wild monster appears!")
        explore()
    elif encounter == "treasure":
        print("You find a hidden treasure chest!")
        Inventory(player).add_item("Gold Coins")
        player.score += 10
        show_status()
    elif encounter == "ally":
        print("You meet a friendly traveler who shares wisdom.")
        player.intelligence += 1
        show_status()
    else:
        print("Nothing happens. The journey continues peacefully.")

def main():
    print("Type 'explore' to begin your adventure, or 'quit' to exit.")
    while True:
        command = input("> ")
        if command.lower() == "explore":
            explore()
        elif command.lower() == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command. Try again.")
            print("Valid commands are: explore, quit")

if __name__ == "__main__":
    main()

def player_death():
    if player.health <= 0:
        print(f"{player.name} has fallen in battle.")
        print("Game Over.")
    return False

def fast_travel(destination):
    print(f"You fast travel to the {destination}.")
    if destination.lower() == "village":
        village()
    elif destination.lower() == "cave":
        cave()
    elif destination.lower() == "abandoned castle":
        abandoned_castle()
    else:
        print("Unknown destination.")
        return

def save_game():
    print("Game saved successfully.")

player_stats = Stats(player)
player_skills = Skills(player)
player_inventory = Inventory(player)
