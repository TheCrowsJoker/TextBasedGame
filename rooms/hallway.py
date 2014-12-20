from rooms.room import Room
from objects.door import Door

class Entranceway(Room):

    def __init__(self):

        self.name = "Entranceway"
        self.description = "You stand in what appears to be a entranceWay. In front of you seems to be the door to exit the mansion."

        self.doors = [
            Door("Open door", "Door", "Dungeon")
        ]

        self.items = []
