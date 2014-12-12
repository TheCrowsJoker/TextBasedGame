import sys

class Escape(object):

    def __init__(self):

        print(sys.version)
        self.createRooms()

    def createRooms(self):
        self.room = {}

    def start(self):
        print("Welcome to ESCAPE!!!!")
        print("  Enjoy your stay.")
        print("")
        
    def end(self):
        print("Thank you for playing!")
        playAgain = input("Would you like to play again (y/n)?")

        if playAgain.lower() is "y":
            self.start()
        else:
            sys.exit()
