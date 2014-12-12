import sys
from rooms.dungeon import Dungeon

class Escape(object):

    def __init__(self):

        print(sys.version)
        self.createRooms()

    def createRooms(self):
        self.rooms = {
            "Dungeon": Dungeon()
        }

    def start(self):
        print("Welcome to ESCAPE!!!!")
        print("Enjoy your stay.")
        print("")

        room = self.rooms["Dungeon"]
        print(room.name)
        print(room.description)

        print("Options:")
        for door in room.doors:
            print("["+door.button + "]" + door.name)

        print("")
        buttonPressed = input(">>> ")
        
    def end(self):
        print("Thank you for playing!")
        playAgain = input("Would you like to play again (y/n)?")

        if playAgain.lower() is "y":
            self.start()
        else:
            sys.exit()
