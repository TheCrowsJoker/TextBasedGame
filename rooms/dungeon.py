from rooms.room import Room
from objects.door import Door

class Dungeon(Room):

    def __init__(self):

        self.name = "Dungeon"
        self.description = "You stand in a gloomy, dark dungeon. there is only one door out but it is locked. However there is a mysterios leaver hidden behind a candlestick."

        self.doors = [
            Door("open door", "Door", "Locked"),
            Door("Pull lever", "Cadlestick", "Tunnel")
        ]

        self.items = []
