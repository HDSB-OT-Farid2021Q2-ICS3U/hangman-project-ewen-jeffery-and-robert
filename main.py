import os
import random
from random_word import RandWord
import drawing
import time
import drawing

def clear(): os.system('cls' if os.name == 'nt' else 'clear')
userLetterList = []
printList = []
wrongList = []
chance = 6

def isLetterInGuessWord(guessLetter, guessWord):
    if guessLetter in guessWord:
        if guessLetter in userLetterList:
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
        drawing.clear()
        drawing.startDraw(word)
        print(f"You guessed the word ({guessingWord}), game is over")
        newgame = input("Would you like to play again? (Y/N): ")
        if newgame.lower() == "y":
            drawing.t.clear()
            clear()
            drawing.startDraw("")
        else:
            exit()

def prtList():
    for o in printList:       
        print(o, end=" ")
    print("")

def hint():
    if hints.lower() == "y":
        hint = []
        hint = [i for i in guessingWord if i not in printList]
        chance = random.randrange(4)
        if chance == 1:
            print(f"Here's a hint, try: {hint[random.randrange(len(hint))]}")

clear()
gametype = input("Do you want to start with a random word or input a word?(R/I): ")
if gametype.lower()== "r":
    guessingWord = RandWord()
else:
    guessingWord = input("Enter the word to be guessed:\n")
done = True
clear()
hints = input("Would you like hints? (Y/N): ")
clear()

for j in range(0, len(guessingWord)):
    print("_ ", end= "")
print("")
word = "_ " * len(guessingWord)

while True:
    drawing.startDraw(word)
    gLetter = input("Enter a letter: ")
    if len(gLetter) >= 2:
        print("Invalid Input")
        continue
    isLetterInGuessWord(gLetter, guessingWord)
    if gLetter not in guessingWord and gLetter not in wrongList:
        chance -= 1
        print(f"You have {chance} chances left")
        wrongList.append(gLetter)
        drawing.drawParts(drawing.t ,chance)
    elif gLetter in wrongList:
        print("It is already guessed")
    if chance == 0:
        drawing.drawParts(drawing.t ,chance)
        clear()
        print("Lose")
        print(f"The word is {guessingWord}")
        exit()
    makePrtList()
    prtList()
    word = ' '.join(printList)
    gameover()
    hint()
    drawing.clear()
    
# TODO: Print invalid input when more than one letter entered
# TODO: Integrate drawing (ALMOST DONE?) @Robert's job
# TODO: Give option to replay screen (@Robert has started in gameOver function)