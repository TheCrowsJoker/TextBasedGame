from rooms.room import Room
from objects.door import Door

class DeadEnd(Room):
    
    def __init__(self):

        self.name = "Dead end"
        self.description = "You walk right into a dead end. There is no way forward. You must turn around and go back from whence you came."

        self.doors = [
            Door("Go back", "Dead end", "Tunnel")
        ]

        self.items = []
