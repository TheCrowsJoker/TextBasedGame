from rooms.room import Room
from objects.door import Door

class Entranceway(Room):

    def __init__(self):

        self.name = "Entranceway"
        self.description = "You stand in what appears to be a entranceway. In front of you seems to be the door to exit the mansion. However, the door is gaurded by and undead VAMPIRE."

        self.doors = [
            Door("Kill vampire", "Exit the building", "Outside", "Crucifix"),
            Door("Go back", "Go back into the ballroom", "Ballroom")
        ]

        self.items = []
