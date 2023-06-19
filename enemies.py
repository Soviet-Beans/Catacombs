#class

class Enemy():
    def __init__(self, name, hp, ac, dmg, val):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.val = val
        self.dmg = dmg
    def __str__ (self):
        return f"{self.name} hp {self.hp} ac {self.ac}"


#Enemies

blank = Enemy('Blank', 99, 99, 99, 99)
rogue = Enemy('Rogue', 5, 0, 2, 3)
knight = Enemy('Knight', 5, 1, 3, 4)
gold = Enemy('Pile of gold', 1, 0, 0, 10)