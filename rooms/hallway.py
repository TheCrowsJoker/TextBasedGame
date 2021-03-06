from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Hallway(Room):

    def __init__(self):

        self.name = "Hallway"
        self.description = "You stand in a hallway that stretches both left and right. There is a door at each end and one more door half way down that leads into the dungeon. There is a sword hanging on one of the walls."

        self.doors = [
            Door("Enter dungeon", "Go into the dungeon", "Dungeon", "Green key"),
            Door("Enter library", "Go back into the library", "Library"),
            Door("Enter next room", "Go forwards into the next room", "Dining Room")
        ]

        self.items = [
        	Item("Take sword", "Sword")
        ]
