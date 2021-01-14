import os
clear = lambda: os.system('cls') # Clear Screen Function

def prtW(wordToGuess,*CorrectLettersGuessed): # Display/Print Word Function
    clear()
    out =""
    length = len(CorrectLettersGuessed) # Length of correct letters
    for x in wordToGuess: # Loop through each letter of the chosen string
        emptyspace = True # Set printing empty space as true in default
        for y in range(1,length+1): # Check letters user has guessed
            if x == CorrectLettersGuessed[y-1]:
                emptyspace = False # Disable printing empty space
                out = (out + x + " ") # Print it and break loop
                break
        if emptyspace == True:
            out= (out + "_ ") # Print empty spaces
    return out
# prtW("HelloWorld","e","o") Testing statement

#TODO:Add statistics to tell the user what letter has already been guessed
if __name__ == "__main__":
    prtW()