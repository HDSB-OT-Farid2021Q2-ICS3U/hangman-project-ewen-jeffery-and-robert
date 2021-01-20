import os
import random
from random_word import RandWord
import drawing
import time
import drawing
import turtle
# Imports and files

# Clear Function
def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def isLetterInGuessWord(guessLetter, guessWord):
    ''' If the letter use guessed is correct, 
    put it into the right list'''
    if guessLetter in guessWord:
        if guessLetter in userLetterList:
            print("\033[91mIt is already guessed\033[0m")
        else:
            userLetterList.append(gLetter)

def makePrtList():
    ''' Make the list that displays the word with underscores'''
    printList.clear()
    [printList.append(x) if x in userLetterList \
else printList.append("_") for x in guessingWord]

def gameover():
    ''' Check if the game is over, if all letters 
    were guessed, ask user to replay or not '''
    done = True

    for a in guessingWord:
        if a not in printList:
            done = False

    if done == True:
        drawing.clearWrite()
        drawing.startDraw(word)
        print(f"\033[1;32;40mYou guessed the word ({guessingWord}),\
 game is over\033[0m")
        newgame = input("\033[91mWould you like to \
play again? (Y/N): \033[0m")
        if newgame.lower() == "y":
            clear()
            drawing.reset(t)
            Start()
        else:
            exit()
    elif killswitch == True:
        newgame = input("\033[91mWould you like to \
play again? (Y/N): \033[0m")
        if newgame.lower() == "y":
            clear()
            drawing.reset(t)
            Start()
        else:
            exit()

def prtList():
    ''' print the Printlist that has 
    been made in the function above '''
    [print(o, end = " ") for o in printList]
    print("")

def hint():
    ''' Give the player hints if the player wants'''
    if hints.lower() == "y":
        hint = []
        hint = [i for i in guessingWord if i not in printList]
        chance = random.randrange(4)
        if chance == 1:
            print(f"\033[96mHere's a hint, try: \
{hint[random.randrange(len(hint))]}\033[0m")

def Start():
    ''' Initialize all variables, checks to see
    if user plays 1 or 2 player, starts game'''
    global userLetterList, printList, wrongList, \
killswitch, chance, guessingWord, done, hints, word
    userLetterList = []
    printList = []
    wrongList = []
    killswitch = False
    chance = 6

    clear()

    gametype = input("\033[95mDo you want to start with a random \
word or input a word? (R/I): \033[0m")

    if gametype.lower()== "r":
        guessingWord = RandWord()
    else:
        guessingWord = input("\033[94;215;250mEnter\
 the word to be guessed:\n\033[0m")
    done = True
    clear()
    hints = input("\033[93mWould you like hints? (Y/N): \033[0m")
    clear()

    [print("_ ", end= "") for j in range(0, len(guessingWord))]
    print("")

    word = "_ " * len(guessingWord)

# runs the start function, creates turtle for clearing, hides it
Start()
t = turtle.Turtle()
t.hideturtle()
t.hideturtle()

# Runs while user is still guessing
# Redraws word everytime, checks if right/wrong guess
# Calls functions above at the bottom
while True:
    drawing.startDraw(word)
    gLetter = input("\033[93mEnter a letter: \033[0m")
    if len(gLetter) >= 2:
        print("\033[91mInvalid Input\033[0m")
    isLetterInGuessWord(gLetter, guessingWord)
    if gLetter not in guessingWord and gLetter not in wrongList:
        chance -= 1
        print(f"\033[91mYou have {chance} chances left\033[0m")
        wrongList.append(gLetter)
        drawing.drawParts(chance, t)
    elif gLetter in wrongList:
        print("\033[91mIt is already guessed\033[0m")
    if chance == 0:
        clear()
        print("\033[95mLose\033[0m")
        print(f"\033[94;215;250mThe word is ({guessingWord})\033[0m")
        killswitch = True
        gameover()
    makePrtList()
    prtList()
    word = ' '.join(printList)
    gameover()
    hint()
    drawing.clearWrite()