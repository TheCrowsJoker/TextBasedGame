from rooms.room import Room
from objects.door import Door

class Kitchen(Room):

    def __init__(self):

        self.name = "Kitchen"
        self.description = "You stand in the kitchen. There is a mighty, undead VAMPIRE standing in your way to the next room."

        self.doors = [
            Door("Go back", "Go back out into the windy hallway", "Windy Hallway"),
            Door("Kill vampire", "Kill the vampire and then walk through the door into the next", "Key Room")
        ]

        self.items = []
