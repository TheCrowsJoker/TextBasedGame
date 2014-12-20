from rooms.room import Room
from objects.door import Door

class Hallway(Room):

    def __init__(self):

        self.name = "Hallway"
        self.description = "You stand in a wallway that streches both left and right."

        self.doors = [
            Door("Open door", "Door", "Dungeon")
        ]

        self.items = []
