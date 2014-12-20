from rooms.room import Room
from objects.door import Door

class Tunnel(Room):

    def __init__(self):

        self.name = "Tunnel"
        self.description = "You stand in a dark tunnel. It streches far into the darkness on both sides of you."

        self.doors = [
            Door("Go left", "Tunnel", "Left tunnel"),
            Door("Go right", "Tunnel", "Dead end")
        ]

        self.items = []
