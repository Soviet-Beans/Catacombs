#class

class Enemy():
    def __init__(self, name, hp, ac, dmg, val):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.val = val
        self.dmg = dmg

#Enemies

blank = Enemy('Blank', 99, 99, 99, 99)

#Floor 1
fl1Rogue = Enemy('Rogue', 5, 0, 2, 3)
fl1Knight = Enemy('Knight', 5, 1, 1, 5)
fl1Gold = Enemy('Pile of gold', 1, 0, 0, 10)