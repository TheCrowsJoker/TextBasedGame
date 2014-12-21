from rooms.room import Room
from objects.door import Door

class Outside(Room):
    
    def __init__(self):

        self.name = "Outside"
        self.description = "You leave the building. you have won the game!!!!!!"

        self.doors = []
        self.items = []
