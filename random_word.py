from random import randint


def RandWord():
    try:
        with open("10K.txt", 'r') as Readfile:
            words = Readfile.readlines()
            

             
            return words[randint(0,len(words))].strip("\n")
    except:
        return "Invalid File"

def RandoWord():
    try:
        with open("20K.txt","r") as Reader:
            words = Reader.readlines()
            return words[randint(0,len(words))].strip("\n")
    except:
        return "No dice"