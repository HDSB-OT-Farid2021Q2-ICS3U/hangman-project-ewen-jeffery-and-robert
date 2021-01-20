from random import randint


def RandWord():

    try:
        with open("10K.txt", 'r') as Readfile:
            file = []
            for line in Readfile:
                file.append(line)
            while True:    
                
                 
                return str(file[randint(0,len(file)-1)]).strip("\n")
                        
    except:
        return "Invalid File"


