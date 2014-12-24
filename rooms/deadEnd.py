from rooms.room import Room
from objects.door import Door
from objects.item import Item

class DeadEnd(Room):
    
    def __init__(self):

        self.name = "Dead end"
        self.description = "You walk right into a dead end. There is no way forward. You must turn around and go back from whence you came. On the ground lies what appears to be a map of the mansion."

        self.doors = [
            Door("Go back", "Go back to the tunnel entrance", "Tunnel")
        ]

        self.items = [
        	Item("Take map", "Map")
        ]
