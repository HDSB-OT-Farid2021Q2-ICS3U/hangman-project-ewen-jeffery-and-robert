
#TODO combine all function files into the game file to be added to main.py

from drawing import startDraw
from random_word import RandWord
from main import prtW
import os
def clear(): os.system('cls' if os.name == 'nt' else 'clear')


def main():
    if input("Would you like a randomly generated word? [y/n]: ").lower() == "y":
        word = RandWord()
    else:
        word = input("Please enter a word: ")
    
    startDraw(prtW(word))
    guess = input("input a letter: ").lower



main()