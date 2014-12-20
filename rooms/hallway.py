from rooms.room import Room
from objects.door import Door

class Hallway(Room):

    def __init__(self):

        self.name = "Hallway"
        self.description = "You stand in a wallway that streches both left and right.There is a door at each end and one more door half way down that leads into the dungeon."

        self.doors = [
            Door("Enter dungeon", "Dungeon", "Dungeon"),
            Door("Go back", "Door", "Library"),
            Door("Go forwards", "Door", "Dining Room")
        ]

        self.items = []
