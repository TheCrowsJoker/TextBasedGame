from rooms.room import Room
from objects.door import Door

class LeftTunnel(Room):

    def __init__(self):

        self.name = "Left Tunnel"
        self.description = "You stand at the end of the tunnel. There is a door infront of you as well as on both your right and left. The tunnel strecthes far back behind you."

        self.doors = [
            Door("Go forwards", "Door", "Dragon Room"),
            Door("Go right", "Door", "Pit"),
            Door("Go left", "Door", "Library"),
            Door("Go back", "Tunnel", "Tunnel")
        ]

        self.items = []
