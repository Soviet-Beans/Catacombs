#Potions

class Potion():
    def __init__(self, name, hp, mana, atk):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.atk = atk

blankPot = Potion('BlankPot', 99, 99, 99)
health = Potion('Health Potion', 3, 0, 0)
rage = Potion('Rage Potion', 0, 0, 3)