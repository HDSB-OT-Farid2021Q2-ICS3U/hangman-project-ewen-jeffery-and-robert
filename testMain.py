import os
import random
from random_word import RandWord
import time
from drawing import drawParts

start = time.time()
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
userLetterList = []
printList = []
wrongList = []
chance = 6
def isLetterInGuessWord(guessLetter,guessWord):
    if guessLetter in guessWord:
        if gLetter in userLetterList:
            print("It is already guessed")
        else:
            userLetterList.append(gLetter)
    else:
        wrongList.append(guessLetter)
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
        print(o,end=" ")
    print("")
clear()
gametype = input("Do you want to start with a random word or input a word?(R/I)")
if gametype == "R" or gametype == "r":
    guessingWord = RandWord()
else:
    guessingWord = input("Enter the word to be guessed\n")
done = True
clear()
for j in range(0,len(guessingWord)):
    print("_ ",end="")
print("")
while True:
    gLetter = input("Enter a letter: ")
    isLetterInGuessWord(gLetter,guessingWord)
    if gLetter not in guessingWord:
        chance = chance - 1
        print(f"You have {chance} chances left")
    elif gLetter in wrongList:
        print("It is already guessed")
    if chance == 0:
        print("Lose")
        print(f"The word is {guessingWord}")
        exit()
    makePrtList()
    prtList()
    gameover()
#TODO: Chance will not be used when the wrong letters were guessed more than one time