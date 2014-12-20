import sys
from rooms.dungeon import Dungeon
from rooms.tunnel import Tunnel
from rooms.entranceway import Entranceway
from rooms.deadEnd import DeadEnd
from objects.backpack import Backpack

class Escape(object):

    def __init__(self):

        print(sys.version)
        self.createRooms()
        self.backpack = Backpack()
    def createRooms(self):
        self.rooms = {
            "Dungeon": Dungeon(),
            "Tunnel": Tunnel(),
            "Dead end": DeadEnd()
        }

    def start(self):
        print("Welcome to ESCAPE!!!!")
        print("Enjoy your stay.")
        print("")
        self.enterRoom("Dungeon")
        
    def end(self):
        print("Thank you for playing!")
        print("Would you like to play again (y/n)?")
        playAgain = input(">>> ")

        if playAgain.lower() is "y":
            self.start()
        else:
            sys.exit()

    def enterRoom(self, roomName):
        room = self.rooms[roomName]
        print(room.name)
        print(room.description)
        if room.name == "Outside":
            self.end()
        else:
            self.askWhatToDo(room)

    def askWhatToDo(self, room):    
        # print out the options
        print("Options:")

        # list the door options
        for door in room.doors:
            print ("[" + door.button + "] " + door.name)

        for item in room.items:
            print("[" + item.button + "]" + item.name)

        # ask the user to make a choice
        print("")
        buttonPressed = input(">>> ")
        # try to find a door associated with that button
        chosenDoor = room.getDoorByButton(buttonPressed)
        chosenItem = room.getItemByButton(buttonPressed)
        print(door.leadsTo)
        self.enterRoom(door.leadsTo) #hayley was here, was chosenDoor.leadsTo

    def takeItem(self, item, room):
        room.removeItem(item)
        self.backpack.items.append(item)
        print("Added " + item.name + " to backpack.")
