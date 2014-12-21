from rooms.room import Room
from objects.door import Door

class Tunnel(Room):

    def __init__(self):

        self.name = "Tunnel"
        self.description = "You stand in a dark tunnel. It streches far into the darkness on both sides of you."

        self.doors = [
            Door("Go left", "Go left down the tunnel", "Left Tunnel"),
            Door("Go right", "Go right down the tunnel", "Dead end"),
            Door("Go back", "Go back into the dungeon", "Dungeon")
        ]

        self.items = []
