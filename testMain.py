import os
import random

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
wordList = ["about","hello","understand","important","opposite","he","crescendo"]
randNum = random.randrange(0,len(wordList))
guessingWord = wordList[randNum]
done = True
while True:
    gLetter = input("Enter a letter: ")
    isLetterInGuessWord(gLetter,guessingWord)
    makePrtList()
    prtList()
    gameover()