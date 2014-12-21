from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Ballroom(Room):
    
    def __init__(self):

        self.name = "Ballroom"
        self.description = "You stand in the ballroom. There is an exit on the other side but the DEVIL himself stands in your way."

        self.doors = [
            Door("Go back", "Go back into the dining room", "Dining Room"),
            Door("Kill devil", "Kill the devil and go into the next room", "Entranceway", "Red key")
        ]

        self.items = [
        	Item("Take key", "Blue Key")
        ]
