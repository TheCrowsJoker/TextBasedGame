class Backpack(object):
    def __init__(self):
        self.items = []

    def getItem(self,wantedItemName):
        wantedItem = None
        for item in self.items:
            if item.name == wantedItemName:
                wantedItem = item

        return wantedItem
