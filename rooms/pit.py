from rooms.room import Room
from objects.door import Door

class Pit(Room):

    def __init__(self):

        self.name = "Pit"
        self.description = "You walk through a door and fall to your death. You lose."

        self.doors = []

        self.items = []
