from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Library(Room):

    def __init__(self):

        self.name = "Library"
        self.description = "You stand in a massive library. The door slams shuts and locks itself behind you. There is a door on the other side of the room. There is a green key hidden behind one of the books."

        self.doors = [
            Door("Open door", "Go through the door on the other side of the room", "Hallway"),
            Door("Go back", "Go back into the dragon room", "Dragon Room", "Blue Key")
        ]

        self.items = [
        	Item("Take key", "Green key")
        ]
