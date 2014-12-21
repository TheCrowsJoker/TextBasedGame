from rooms.room import Room
from objects.door import Door

class DiningRoom(Room):
    
    def __init__(self):

        self.name = "Dining Room"
        self.description = "You stand in the dining room. There is a door behind you and a door on the other side but a gigantic BASILISK stands in your way."

        self.doors = [
            Door("Go back", "Go back into the hallway", "Hallway"),
            Door("Kill basilisk", "Kill the basilisk and move onto the next room", "Ballroom"),
            Door("Go left", "Go into the room on your left", "Windy Hallway")
        ]

        self.items = []
