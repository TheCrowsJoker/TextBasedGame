class Room(object):

    def __init__(self):
        pass

    def getDoorByButton(self,buttonPressed):
        chosenDoor = None
        for door in self.doors:
            print(door.button)
            if door.button is buttonPressed:
                chosenDoor = door
        return chosenDoor

    def getItemByButton(self,buttonPressed):
        chosenItem = None
        for item in self.items:
            if item.button is buttonPressed:
                chosenItem = item
        return chosenItem

    def removeItem(self,itemToRemove):
        self.items.remove(itemToRemove)
