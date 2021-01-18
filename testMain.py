import os
import random
from random_word import RandWord
import time
import drawing

start = time.time()
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
userLetterList = []
printList = []
wrongList = []
chance = 6

def isLetterInGuessWord(guessLetter, guessWord):
    if guessLetter in guessWord:
        if gLetter in userLetterList:
            print("It is already guessed")
        else:
            userLetterList.append(gLetter)

def makePrtList():
    printList.clear()
    for x in guessingWord:
        if x in userLetterList:
            printList.append(x)
        else:
            printList.append("_")

def gameover():
    done = True
    for a in guessingWord:
        if a not in printList:
            done = False
    if done == True:
        print(f"You guessed the word ({guessingWord}), game is over")
        exit()

def prtList():
    for o in printList:       
        print(o, end=" ")
    print("")
clear()
gametype = input("Do you want to start with a random word or input a word?(R/I)")
if gametype == "R" or gametype == "r":
    guessingWord = RandWord()
else:
    guessingWord = input("Enter the word to be guessed\n")
done = True
clear()
for j in range(0, len(guessingWord)):
    print("_ ", end="")
print("")

while True:
    drawing.startDraw(guessingWord)
    gLetter = input("Enter a letter: ")
    if len(gLetter)>=2:
        print("Invalid Input")
        continue
    isLetterInGuessWord(gLetter, guessingWord)
    if gLetter not in guessingWord and gLetter not in wrongList:
        chance -= 1
        print(f"You have {chance} chances left")
        wrongList.append(gLetter)
        drawing.drawParts(chance, t)
    elif gLetter in wrongList:
        print("It is already guessed")
    if chance == 0:
        print("Lose")
        print(f"The word is {guessingWord}")
        exit()
    makePrtList()
    prtList()
    gameover()
#TODO: Print invalid input when more than one letter entered