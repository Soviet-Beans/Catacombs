#class

class Enemy():
    def __init__(self, name, hp, ac):
        self.name = name
        self.hp = hp
        self.ac = ac
    def __str__ (self):
        return f"{self.name} hp {self.hp} ac {self.ac}"


#Enemies

rogue = Enemy('Rogue', 5, 0)