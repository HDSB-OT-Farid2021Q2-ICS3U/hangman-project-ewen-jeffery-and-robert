from drawing import startDraw
from random_word import RandWord

import os
def cls(): os.system('cls' if os.name == 'nt' else 'clear')

cls()
if input("Would you like a random word?[Y/N]:").lower() == 'y':
    word = RandWord()
else: 
    word = input("Please input a word: ")
cls()
print(word)


