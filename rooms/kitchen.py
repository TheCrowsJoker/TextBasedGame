from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Kitchen(Room):

    def __init__(self):

        self.name = "Kitchen"
        self.description = "You stand in the kitchen. There is a mighty, TROLL standing in your way to the next room."

        self.doors = [
            Door("Go back", "Go back out into the windy hallway", "Windy Hallway"),
            Door("Hit troll with axe", "Kill the Troll and then walk through the door into the next room", "Key Room", "Axe")
        ]

        self.items = [
       		Item("Take key", "Black key")
       	]
