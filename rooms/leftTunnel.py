from rooms.room import Room
from objects.door import Door

class LeftTunnel(Room):

    def __init__(self):

        self.name = "Left Tunnel"
        self.description = "You stand at the end of the tunnel. There is a door in front of you as well as one on your right. The tunnel stretches far back behind you."

        self.doors = [
            Door("Go forwards", "Go into the room in front of you", "Dragon Room"),
            Door("Go right", "Go into the room on your right", "Pit"),
            Door("Go back", "Go back down the tunnel", "Tunnel")
        ]

        self.items = []
