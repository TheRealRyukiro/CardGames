# Imports
from Card import Card
from time import sleep
from os import system
from sys import stdout
# Predefined Variables
GAMES = ["Blackjack (WIP)", "War (Coming soon...)", "Poker (Coming soon...)"]
VERSION = 0.01

DISPLAYGAMES = (
    f"""
    Welcome to Tommy's card games v{VERSION}!
    Type the Game you would like to play:
    """
)
for Game in GAMES:
    DISPLAYGAMES += (
    f"""
        - {Game}
    """
    )

DISPLAYGAMES += (
    """
    Type Exit to quit the game...
    """
)
def magicText(text, speed):
    for letter in text:
        stdout.write(letter)
        stdout.flush()
        sleep(speed)
    print("\n")
def clearScreen():
    system("clear")
def mainLoop(Testing = False):
    clearScreen()
    if not Testing: #If I quickly want to test something and don't want to go through the whole game loop I'll set Testing to True
        answer = ""
        print(DISPLAYGAMES)
        while answer != "exit":
            answer = input("> ").lower()
            if(answer == "blackjack" or answer == "black jack"):
                clearScreen()
                while answer != "exit":
                    print()
                    answer = input("> ").lower()


            elif(answer == "war"):
                pass
            elif(answer == "poker"):
                pass
            elif(answer == "games" or answer.lower() == "game"):
                clearScreen()
                print(DISPLAYGAMES)
            elif(answer == "exit"):
                clearScreen()
                print("Thank you for playing Tommy's card games!")
                sleep(1)
                print("Please come back soon!")
                sleep(2)
            else:
                print(f"Sorry, {answer} is not a valid choice. Please check your spelling and try again. Type games if you want to see the list of games")
    elif Testing:
        magicText("Entered Testing Mode...", 0.05)
        pass

if __name__ == "__main__": mainLoop(True)
