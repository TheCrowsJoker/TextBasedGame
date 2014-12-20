from rooms.room import Room
from objects.door import Door

class Ballroom(Room):
    
    def __init__(self):

        self.name = "Ballroom"
        self.description = "You stand in the ballroom. There is an exit on the other side but the DEVIL himself stands in your way."

        self.doors = [
            Door("Go back", "Door", "Dining Room"),
            Door("Kill devil", "Devil", "Entranceway")
        ]

        self.items = []
