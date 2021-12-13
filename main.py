
from pics import *
from Game import *


# Spiel


# print(map_arr)


print("\n\n")
print(logo)
# print("Willkommen auf der Schlangen-Insel!")
# name = input("Wie lautet dein Name?")
# print("Hallo " + name)

myGame = Game()

while True:
    print(f"\n-- Runde {myGame.runde} --")
    myGame.printEvents()
    myGame.printTopoInfo()
    myGame.showMap()
    
    myGame.userInput()

    myGame.handleEndOfRound()


exit()
