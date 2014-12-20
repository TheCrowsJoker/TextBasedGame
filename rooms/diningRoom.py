from rooms.room import Room
from objects.door import Door

class DiningRoom(Room):
    
    def __init__(self):

        self.name = "Dining Room"
        self.description = "You stand in the sining room. there is a door behind you and a door on the other side but a gigantic BASILISK stands in your way."

        self.doors = [
            Door("Go back", "Door", "Hallway"),
            Door("Kill basilisk", "Door", "Ballroom")
        ]

        self.items = []
