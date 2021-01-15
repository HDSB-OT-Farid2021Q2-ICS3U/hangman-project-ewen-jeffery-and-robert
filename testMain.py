import os
import random
from random_word import RandWord
import time

start = time.time()
def clear(): os.system('cls' if os.name == 'nt' else 'clear')
userLetterList = []
printList = []
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
