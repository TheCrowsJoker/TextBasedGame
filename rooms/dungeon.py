from rooms.room import Room
from objects.door import Door

class Dungeon(Room):

    def __init__(self):

        self.name = "Dungeon"
        self.description = "You stand in a gloomy, dark dungeon. There is only one door out but it is locked. However there is a mysterios lever hidden behind a candlestick."

        self.doors = [
            Door("Open door", "Try to open the door", "Hallway", "Green key"),
            Door("Pull lever", "Pull on the cadlestick", "Tunnel")
        ]

        self.items = []
