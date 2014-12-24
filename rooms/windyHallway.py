from rooms.room import Room
from objects.door import Door
from objects.item import Item

class WindyHallway(Room):

    def __init__(self):

        self.name = "Windy Hallway"
        self.description = "You stand in a long windy hallway. There is a door at one end and the door that you just came through. There is a bloody axe lying in the center of the hallway."

        self.doors = [
            Door("Go back", "Go back out into the Dining room", "Dining Room"),
            Door("Go forwards", "Go through the door into the next room", "Kitchen")
        ]

        self.items = [
        	Item("Take axe", "Axe")
        ]
