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

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

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

def floor1():
    playerData.gold = playerData.gold + 1
    playerData.hp = playerData.hp + 1
    playerData.ac = playerData.ac + 1
    playerData.dmg = playerData.dmg + 1
    print(playerData.gold, playerData.hp, playerData.ac, playerData.dmg)
    time.sleep(3)
    mainMenu()

def floor2():
    clearConsole()
    playerData.loadGame()
    time.sleep(3)
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