
#imports
import random

#the teens want peggy.
#global number, decided at runtime
HIDDENNUM = random.randint(1, 100)

#create global int 1 - 100
#ask user to enter a number
#if they guess correct then exit
#if they guess wrong let them know high or low then recurse
print("\n\n\n\n\n\n\n\n\n\n\n\n\nGuess a number 1 through 100: ")

def askNum():
    """Asks the user for their guess, and checks the type of the input before handing it to the main function. """
    uGuesss = str(input())
    if uGuesss.isnumeric():
        uGuesss = int(uGuesss)
    else:
        print("that won't work")
        playGame()
    return uGuesss

def playGame():
    """Runs the game itself, present for recursion"""
    uGuess = askNum()

    if (uGuess < HIDDENNUM):
        print("higher")
        playGame()
    elif (uGuess > HIDDENNUM):
        print("lower")
        playGame()
    elif (uGuess == HIDDENNUM):
        print("You Got it!")
        exit()

playGame()
