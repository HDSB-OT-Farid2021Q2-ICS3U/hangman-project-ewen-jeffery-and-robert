import os
import random
from random_word import RandWord
<<<<<<< HEAD
clear = lambda: os.system('cls') # Clear Screen Function
=======
import time

start = time.time()
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
>>>>>>> c9917ab9e3158c36e5b39a8b0179257abd876345
userLetterList = []
printList = []
chance = 5
def isLetterInGuessWord(guessLetter,guessWord):
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
        print(o,end=" ")
    print("")
<<<<<<< HEAD
clear()
gametype = input("Do you want to start with a random word or input a word?(R/I)")
if gametype == "R" or gametype == "r":
    guessingWord = RandWord()
else:
    guessingWord = input("Enter the word to be guessed")
done = True
clear()
while True:
    gLetter = input("Enter a letter: ")
    if gLetter not in guessingWord:
        chance = chance - 1
    if chance == 0:
        print("Lose")
        exit()
    isLetterInGuessWord(gLetter,guessingWord,)
    makePrtList()
    prtList()
    input("")
    clear()
    prtList()
    gameover()
=======
guessingWord = RandWord()
done = True 
while True:
    gLetter = input("Enter a letter: ")
    if len(gLetter) == 1 and gLetter.isdigit == False:
        isLetterInGuessWord(gLetter,guessingWord)
    else:
        continue
    makePrtList()
    prtList()
    gameover()
>>>>>>> c9917ab9e3158c36e5b39a8b0179257abd876345
