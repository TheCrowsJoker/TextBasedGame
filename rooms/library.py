from rooms.room import Room
from objects.door import Door

class Library(Room):

    def __init__(self):

        self.name = "Library"
        self.description = "You stand in a massive library. The door slams shuts and locks itself behind you. There is a door on the other side of the room."

        self.doors = [
            Door("Go forwards", "Door", "Hallway")
        ]

        self.items = []
