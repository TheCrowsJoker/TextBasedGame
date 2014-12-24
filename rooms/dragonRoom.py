from rooms.room import Room
from objects.door import Door

class DragonRoom(Room):

    def __init__(self):

        self.name = "Dragon Room"
        self.description = "You stand in a massive room with only the door behind you and one other door out. The only problem is a massive DRAGON stands in your way."

        self.doors = [
            Door("Go back", "Go back out into the tunnel", "Left Tunnel"),
            Door("Kill dragon", "Kill the dragon and then walk through the door into the next room", "Library", "Bone")
        ]

        self.items = []
