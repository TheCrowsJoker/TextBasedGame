import sys

## Rooms
from rooms.dungeon import Dungeon
from rooms.tunnel import Tunnel
from rooms.entranceway import Entranceway
from rooms.deadEnd import DeadEnd
from rooms.hallway import Hallway
from rooms.leftTunnel import LeftTunnel
from rooms.pit import Pit
from rooms.dragonRoom import  DragonRoom
from rooms.library import Library
from rooms.diningRoom import DiningRoom
from rooms.ballroom import Ballroom
from rooms.outside import Outside
from rooms.windyHallway import WindyHallway
from rooms.kitchen import Kitchen
from rooms.keyRoom import KeyRoom

## Objects
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
            "Entranceway": Entranceway(),
            "Dead end": DeadEnd(),
            "Hallway": Hallway(),
            "Left Tunnel": LeftTunnel(),
            "Dragon Room": DragonRoom(),
            "Library": Library(),
            "Ballroom": Ballroom(),
            "Dining Room": DiningRoom(),
            "Outside": Outside(),
            "Pit": Pit(),
            "Windy Hallway": WindyHallway(),
            "Kitchen": Kitchen(),
            "Key Room": KeyRoom()
        }

    def start(self):
        print("")
        print("")
        print("Welcome to ESCAPE!!!!")
        print("Enjoy your stay.")
        print("Type in the commands in the square brackets to play.")
        print("Type 'Backpack' at any time to view what items you have.")
        print("")
        self.enterRoom("Dungeon")
        
    def end(self):
        print("Thank you for playing!")
        print("Would you like to play again (y/n)?")
        playAgain = input(">>> ")

        if playAgain.lower() == "y" or playAgain.lower() == "yes":
            self.start()
        elif playAgain.lower() == "n" or playAgain.lower() == "no":
            sys.exit()
        else:
            self.end()


    def openDoor(self, door, room):
        if door.requiredItem == None:   
            self.enterRoom(door.leadsTo)
        else:
            item = self.backpack.getItem(door.requiredItem)

            if item != None:
                print("Used " + item.name)
                self.enterRoom(door.leadsTo)
            else:
                print("It looks like you need a " + door.requiredItem)
                self.askWhatToDo(room)


    def enterRoom(self, roomName):
        room = self.rooms[roomName]
        print(room.name)
        print(room.description)
        if room.name == "Outside" or room.name == "Pit":
            self.end()
        else:
            self.askWhatToDo(room)

    def askWhatToDo(self, room):    
        # print out the options
        print("")
        print("Options:")

        # list the door options
        for door in room.doors:
            print ("[" + door.button + "] " + door.name)

        for item in room.items:
            print("[" + item.button + "] " + item.name)

        # ask the user to make a choice
        print("")
        buttonPressed = input(">>> ")
        print("")
        if buttonPressed == "Backpack":
            if len(self.backpack.items) == 0:
                print("You currently have no items in your backpack")
            else:
                print("Items in your backpack:")
                for item in self.backpack.items:
                    print("    " + item.name)
            print("")
            self.askWhatToDo(room)
        else:
            # try to find a door associated with that button
            chosenDoor = room.getDoorByButton(buttonPressed)
            # find item associated with that button
            chosenItem = room.getItemByButton(buttonPressed)

            if chosenDoor == None and chosenItem == None:
                print("This is not a valid input!")
                print("Please try again")
                self.askWhatToDo(room)
            else:
                if chosenDoor != None:
                    self.openDoor(chosenDoor, room)
                elif chosenItem != None:
                    self.takeItem(chosenItem, room)
                    self.askWhatToDo(room)
    
    def takeItem(self, item, room):
        room.removeItem(item)
        self.backpack.items.append(item)
        print("Added " + item.name + " to backpack.")
