from rooms.room import Room
from objects.door import Door

class EntranceWay(Room):

    def __init__(self):

        self.name = "EntranceWay"
        self.description = "You stand in what appears to be a entranceWay. In front of you seems to be the door to exit the mansion."

        self.doors = [
            Door("Open door", "Door", "Outside"),
            Door("Open door", "Door", "Ballroom")
        ]

        self.items = []
