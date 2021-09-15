# Imports
from Card import Card
from time import sleep
from os import system

# Predefined Variables
GAMES = ["Blackjack (WIP)", "War (Coming soon...)", "Poker (Coming soon...)"]

DISPLAYGAMES = (
    """
    Type the Game you would like to play:
    """
)
for game in GAMES:
    DISPLAYGAMES += (
    f"""
        - {game}
    """
    )

DISPLAYGAMES += (
    """
    Type Exit to quit the game...
    """
)
def clearScreen():
    system("clear")
def mainLoop():
    clearScreen()
    answer = ""
    print(DISPLAYGAMES)
    while answer.lower() != "exit":
        answer = input("> ")
        if(answer.lower() == "blackjack" or answer.lower() == "black jack"):
            pass
        elif(answer.lower() == "war"):
            pass
        elif(answer.lower() == "poker"):
            pass
        elif(answer.lower() == "games" or answer.lower() == "game"):
            clearScreen()
            print(DISPLAYGAMES)
        elif(answer.lower() == "exit"):
            clearScreen()
            print("Thank you for playing Tommy's card games! Please come back soon!")
            sleep(2)
        else:
            print(f"Sorry, {answer} is not a valid choice. Please check your spelling and try again. Type games if you want to see the list of games")

if __name__ == "__main__": mainLoop()
