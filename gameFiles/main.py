# Libraries
import sys
import random
import os
import math
import time

#Other Files
import enemies
import playerData
import items

#Logic
currentEnemy = enemies.blank
enemyhp = currentEnemy.hp

usedPotion = items.blankPot
bonusDmg = 0
bonusHp = 0
def potionBoost():
    global bonusDmg, bonusHp
    bonusDmg = usedPotion.atk
    bonusHp = usedPotion.hp
    playerData.hp = playerData.hp + bonusHp
    if playerData.hp >= 10:
        playerData.hp = 10

enemyDmg = 0
def enemyHit():
    global enemyDmg
    enemyDmg = currentEnemy.dmg - playerData.ac

playerDmg = 0
def playerHit():
    global playerDmg, enemyhp
    playerDmg = playerData.dmg - currentEnemy.ac + bonusDmg
    enemyhp = enemyhp - playerDmg

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

generate = 0
def generateDungeon():
    global generate
    generate = random.randrange(1, 6)

def fight():
    clearConsole()
    if playerData.hp <= 0:
        playerData.hp = 10
        print('You have died')
        playerData.gold = playerData.gold - (playerData.gold // 2)
        print('you have lost', playerData.gold, 'gold')
        time.sleep(2)
        mainMenu()
    else:
        print('You encounterd a', currentEnemy.name)
        print('You have', playerData.hp, 'HP')
        print('')
        print('What would you like to do?')
        print('')
        print('Attack (1)')
        print('Use Item (2)')
        print('')
        playerIn = input()
        print('')
        if playerIn in ['1']:
            playerHit()
            if enemyhp <= 0:
                print(currentEnemy.name,'defeated')
                print('You gained', currentEnemy.val, 'gold')
                playerData.gold = playerData.gold + currentEnemy.val
                print('You now have', playerData.gold,'gold')
                time.sleep(2)
                floor1()
            else:
                print('You dealt', playerDmg, 'damage')
                time.sleep(1)
                clearConsole()
                enemyHit()
                playerData.hp = playerData.hp - enemyDmg
                print('You took', enemyDmg, 'damage')
                print('You now have', playerData.hp, 'HP')
                time.sleep(1)
                fight()
    if playerIn in ["2"]:
        print('Which item would you like to use? ')
        print('')
        print('Health Potion (1)', playerData.health)
        print('Rage Potion (2)', playerData.rage)
        playerInp = input()
        global usedPotion
        if playerInp in ['1']:
            if playerData.health >= 1:
                usedPotion = items.health
                playerData.health = playerData.health - 1
                potionBoost()
                print('you now have', playerData.hp, 'HP')
                time.sleep(1)
            else:
                print('You do not have enough potions')
                time.sleep(1)
            fight()
        if playerInp in ['2']:
            if playerData.rage >= 1:
                usedPotion = items.rage
                playerData.rage = playerData.rage - 1
                potionBoost()
                print('You now do', bonusDmg, 'Bonus Damage')
                time.sleep(1)
                fight()
            else:
                print('You do not have enough potions')
                time.sleep(1)
            fight()
        else:
            print('That is not a valid input')
            time.sleep(1)
            fight()


#intro
name = input('What is your name? ')

#Main Menu
def mainMenu():
    global bonusDmg
    bonusDmg = 0
    playerData.hp = 10
    clearConsole()
    print('Welcome to the catacombs', name)
    print('')    
    print('What would you like to do?')
    print('')
    print('Enter the catacombs (1)')
    print('Enter the shop (2)')
    print('Save Game (3)')
    print('Quit (4)')
    print('')
    playerin = input()
    if playerin in ['1']:
        clearConsole()
        print('Please select floor')
        print('1')
        floorSelect = input()
        if floorSelect in ['1']:
            floor1()
        else:
            print('That is an invalid input')
    elif playerin in ['2']:
        shop()
    elif playerin in ['3']:
        playerData.saveGame()
        mainMenu()
    elif playerin in ['4']:
        clearConsole()
        quit = input('Are you sure you want to quit? (y/n) ')
        if quit in ['y', 'Y', 'yes', 'Yes', 'YES', 'YEs', 'yES', 'YeS', 'yEs', 'yeS']:
            sys.exit()
        elif quit in ['n', 'N', 'No', 'NO', 'nO']:
            mainMenu()
    else:
        print('That is not a valid input')
        time.sleep(1)
        mainMenu()


#Floors

counter = 0
def floor1():
    clearConsole()
    global counter, bonusDmg
    bonusDmg = 0
    counter = counter + 1
    if counter == 10:
        print('Floor Defeated')
        time.sleep(1)
        mainMenu()
    else:
        global currentEnemy, enemyhp
        generateDungeon()
        if generate ==  1:
            currentEnemy = enemies.fl1Knight
        if generate == 2:
            currentEnemy = enemies.fl1Rogue
        if generate == 3:
            currentEnemy = enemies.fl1Rogue
        if generate == 4:
            currentEnemy = enemies.fl1Rogue
        if generate == 5:
            currentEnemy = enemies.fl1Gold
        enemyhp = currentEnemy.hp
        fight()

    time.sleep(2)
    mainMenu()
def floor2():
    playerHit()
    print(playerDmg)
    time.sleep(1)
    mainMenu()
#Shop

def shop():
    clearConsole()
    print('Welcome to the shop')
    print('You have', playerData.gold, 'gold')
    print('What would you like to purchase?')
    print('')
    print('Health Potion (2 gold) (1)')
    print('Rage Potion (2 gold) (2)')
    print('Exit shop (3)')
    print('')
    playerin = input()
    if playerin in ['1']:
        clearConsole()
        print('How many would you like to buy?')
        print('')
        playerin = int(input())
        try:
            int(playerin)
            if playerData.gold >= 2 * playerin:
                playerData.health = playerData.health + playerin
                print('Succesfully purchased', playerin, 'Health Potions')
                time.sleep(1)
                shop()
            else:
                print("You don't have enough money")
                time.sleep(1)
                shop()
        except ValueError:
            print('That is not a valid input')
            time.sleep(1)
            shop()
    if playerin in ['2']:
        clearConsole()
        print('How many would you like to buy?')
        print('')
        playerin = int(input())
        try:
            int(playerin)
            if playerData.gold >= 2 * playerin:
                playerData.rage = playerData.rage + playerin
                print('Succesfully purchased', playerin, 'Rage Potions')
                time.sleep(1)
                shop()
            else:
                print("You don't have enough gold")
                time.sleep(1)
                shop()
        except ValueError:
            print('That is not a valid input')
            time.sleep(1)
            shop()
    if playerin in ['3']:
        mainMenu()
    else:
        print('That is not a valid input')
        time.sleep
        shop()

playerData.loadGame
mainMenu()