# Libraries
import sys
import random
import os
import math
import time

#Other Files
import enemies
import playerData

#Logic
currentEnemy = enemies.blank

enemyDmg = 0
def enemyHit():
    global enemyDmg
    enemyDmg = currentEnemy.dmg - playerData.ac

playerDmg = 0
def playerHit():
    global playerDmg
    playerDmg = playerData.dmg - currentEnemy.ac

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
    clearConsole()
    if playerData.hp <= 0:
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
            currentEnemy.hp = currentEnemy.hp - playerDmg
            if currentEnemy.hp <= 0:
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
                fight()
    if playerIn in ["2"]:
        print('Not currently functional')
        time.sleep(1)
        fight()


#intro
name = input('What is your name? ')

#Main Menu
def mainMenu():
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
            currentEnemy = enemies.knight
        if generate == 2:
            currentEnemy = enemies.rogue
        if generate == 3:
            currentEnemy = enemies.rogue
        if generate == 4:
            currentEnemy = enemies.rogue
        if generate == 5:
            currentEnemy = enemies.gold
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
    print(rogue)
    time.sleep(3)
    mainMenu()

#Enemy Imports
rogue = enemies.rogue

playerData.loadGame()
mainMenu()