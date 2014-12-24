from rooms.room import Room
from objects.door import Door
from objects.item import Item

class Ballroom(Room):
    
    def __init__(self):

        self.name = "Ballroom"
        self.description = "You stand in the ballroom. There is an exit on the other side. A crucifix lies on the ground at your feet and a blue key sits on a nearby table."

        self.doors = [
            Door("Go back", "Go back into the dining room", "Dining Room"),
            Door("Go forwards", "Move on into the next room", "Entranceway", "Red key")
        ]

        self.items = [
        	Item("Take key", "Blue Key"),
            Item("Take crucifix","Crucifix")
        ]
