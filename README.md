[![Work in Repl.it](https://classroom.github.com/assets/work-in-replit-14baed9a392b3a25080506f3b7b6d57f295ec2978f6f33ec97e36a161684cbe9.svg)](https://classroom.github.com/online_ide?assignment_repo_id=350247&assignment_repo_type=GroupAssignmentRepo)
# Hangman Assignment

If you haven't played hangman before, the rules are simple: you have to guess a word before it is too late and the body is hung. It's as simple as that!

Our take on hangman involves a 1 and 2 player mode, where you can either guess a randomly generated word or have a friend think of one for you. We also have hints, a literal drawing and much, much more!

## Installation

Just clone the repo. Make sure to run the main.py file as the other files won't do anything on their own.

## Usage

RUN MAIN.PY!

```python
gametype = input("\033[95mDo you want to start with a random word or input a word? (R/I): \033[0m")
```
Our game starts off by asking the user to make a simple choice; to choose which mode to play, 1 player or 2 players. The random word mode allows anyone to play by themselves as the program chooses a random word from a long list. The input word allows one user to input a word to guess and the other to guess it.

Next, the game will ask if you would like to play with hints. Hints are a unique feature in our game: they allow the user to get help if they are struggling. The way it works is that everytime you guess a letter there's a 1/4 chance that the program will tell you one of the remaining letters. This allows for more manageable games when the word is too long.

Afterwards, you're thrown straight in! A separate window will appear, containing a drawing. Don't worry, you can move this window around wherever you deem fit, as long as you don't close it. After that, you will have to keep guessing letters until either all the body parts are drawn or you guess the full word. It will display your spaces for the letters within the word inside the terminal as well as in the turtle drawing. Remember, you cannot input more than 1 character and cannot input the same character more than once. Also, the game is case sensitive, so be aware of that if you're playing in the input mode.

Once you finally end the game, you're presented with another input: whether you want to play again or not. If you say yes, the whole game will restart and you will get to play the whole thing once more. If you say no, then the program will exit.

## Extra Information

For any extra information such as contact info or requirements, please consult the graphic below.
Also this game was coded in python, so please have Python 3.8.6 (or higher) as your software requirement.
![image](https://user-images.githubusercontent.com/74550921/105123159-99b7df00-5aa5-11eb-8ae0-f34ea6a8a66f.png)

(Please don't take the chart too seriously, obviously hardware requirements are the bare minimum for such a small game)