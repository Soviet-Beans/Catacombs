#files
import items

#Stats

gold = 0
hp = 10
ac = 0
dmg = 3

#potions

health = 3
rage = 0

def saveGame():
    goldStr = str(gold)
    hpStr = str(hp)
    acStr = str(ac)
    dmgStr = str(dmg)
    healthStr = str(health)
    rageStr = str(rage)
    save = open('gameFiles\playerData.txt', 'w')
    save.write(goldStr)
    save.write(' ')
    save.write(hpStr)
    save.write(' ')
    save.write(acStr)
    save.write(' ')
    save.write(dmgStr)
    save.write(' ')
    save.write(healthStr)
    save.write(' ')
    save.write(rageStr)

def loadGame():
    load = open('gameFiles\playerdata.txt', 'r')
    for line in load:
        a = line.split()
        print(a)
        global gold, hp, ac, dmg, health, rage
        gold = int(a[0])
        hp = int(a[1])
        ac = int(a[2])
        dmg = int(a[3])
        health = int(a[4])
        rage = int(a[5])