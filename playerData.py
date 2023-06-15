gold = 0
hp = 12
ac = 0
dmg = 2

def saveGame():
    goldStr = str(gold)
    hpStr = str(hp)
    acStr = str(ac)
    dmgStr = str(dmg)
    save = open('playerData.txt', 'w')
    save.write(goldStr)
    save.write(' ')
    save.write(hpStr)
    save.write(' ')
    save.write(acStr)
    save.write(' ')
    save.write(dmgStr)

def loadGame():
    gold = 0
    hp = 0
    ac = 0
    dmg = 0
    load = open('playerdata.txt', 'r')
    for line in load:
        a = line.split()
        print(a)
        gold = int(a[0])
        hp = int(a[1])
        ac = int(a[2])
        dmg = int(a[3])
        print(gold, hp, ac, dmg)