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
def potionBoost():
    global bonusDmg
    bonusDmg = usedPotion.atk

enemyDmg = 0
def enemyHit():
    global enemyDmg
    enemyDmg = currentEnemy.dmg - playerData.ac

playerDmg = 0
def playerHit():
    global playerDmg
    playerDmg = playerData.dmg - currentEnemy.ac + bonusDmg

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

generate = 0
def generateDungeon():
    global generate
    generate = random.randrange(1, 5)

def fight():
    global enemyhp
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
            enemyhp = enemyhp - playerDmg
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
                time.sleep(1)
                fight()
    if playerIn in ["2"]:
        print('Not currently functional')
        time.sleep(1)
        fight()


#intro
name = input('What is your name? ')

#Main Menu
def mainMenu():
    global bonusDmg
    bonusDmg = 0
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
        print('')
        floorSelect = input()
        if floorSelect in ['1']:
            floor1()
        if floorSelect in ['2']:
            floor2()
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
    global counter
    counter = counter + 1
    if counter == 10:
        print('Floor Defeated')
        time.sleep(1)
        mainMenu()
    else:
        generateDungeon()
        if generate ==  1:
            global currentEnemy
            currentEnemy = enemies.fl1Knight
        if generate == 2:
            currentEnemy = enemies.fl1Rogue
        if generate == 3:
            currentEnemy = enemies.fl1Rogue
        if generate == 4:
            currentEnemy = enemies.fl1Rogue
        if generate == 5:
            currentEnemy = enemies.fl1Gold
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
                print("You don't have enough money")
                time.sleep(1)
                shop()
        except ValueError:
            print('That is not a valid input')
            time.sleep(1)
            shop()
    if playerin in ['3']:
        mainMenu()

playerData.loadGame
mainMenu()