from rooms.room import Room
from objects.door import Door
from objects.item import Item

class KeyRoom(Room):

    def __init__(self):

        self.name = "Key Room"
        self.description = "You stand in a small room. There is a door behind you and there is a key hanging on the wall in front of you."

        self.doors = [
            Door("Go back", "Go back out into the kitchen", "Kitchen")        ]

        self.items = [
            Item("Take key", "Red key")
		]
