import os
import random
from random_word import RandWord
import drawing
import time
import drawing
import turtle

#Imports and files

def clear(): os.system('cls' if os.name == 'nt' else 'clear') # Clear Function

def isLetterInGuessWord(guessLetter, guessWord):
    ''' If the letter use guessed is correct, put it into the right list'''
    if guessLetter in guessWord:
        if guessLetter in userLetterList:
            print("It is already guessed")
        else:
            userLetterList.append(gLetter)

def makePrtList():
    ''' Make the list that displays the word with underscores'''
    printList.clear()
    for x in guessingWord:
        if x in userLetterList:
            printList.append(x)
        else:
            printList.append("_")

def gameover():
    ''' Check if the game is over, if all letters were guessed, ask user to replay or not '''
    done = True
    for a in guessingWord:
        if a not in printList:
            done = False
    if done == True:
        print(f"You guessed the word ({guessingWord}), game is over")
        newgame = input("Would you like to play again? (Y/N): ")
        if newgame.lower() == "y":
            clear()
            drawing.clear(t)
            Start()
        else:
            exit()
    elif killswitch == True:
        newgame = input("Would you like to play again? (Y/N): ")
        if newgame.lower() == "y":
            clear()
            drawing.clear(t)
            Start()
        else:
            exit()

def prtList():
    ''' print the Printlist that has been made in the function above '''
    for o in printList:       
        print(o, end = " ")
    print("")

def hint():
    ''' Give the player hints if the play wants'''
    if hints.lower() == "y":
        hint = []
        hint = [i for i in guessingWord if i not in printList]
        chance = random.randrange(4)
        if chance == 1:
            print(f"Here's a hint, try: {hint[random.randrange(len(hint))]}")

def Start():
    ''' Initialize all variables'''
    global userLetterList, printList, wrongList, killswitch, chance, guessingWord, done, hints
    userLetterList = []
    printList = []
    wrongList = []
    killswitch = False
    chance = 6

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
    global word
    word = "_ " * len(guessingWord)

Start()
t = turtle.Turtle()
t.hideturtle()
t.hideturtle()

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
        drawing.drawParts(chance, t)
    elif gLetter in wrongList:
        print("It is already guessed")
    if chance == 0:
        clear()
        print("Lose")
        print(f"The word is {guessingWord}")
        killswitch = True
        gameover()
    makePrtList()
    prtList()
    word = ' '.join(printList)
    gameover()
    hint()
    drawing.clearRight()

# TODO: Print invalid input when more than one letter entered(Fixed) @Jeffery
# TODO: Integrate drawing (ALMOST DONE?) @Robert's job
# TODO: Give option to replay screen (@Robert has started in gameOver function)