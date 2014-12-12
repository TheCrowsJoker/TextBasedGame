class Room(object):

	def __init__(self):
		pass
	

	# get the door object related to the key that was pressed
	def getDoorByButton(self, buttonPressed):

		chosenDoor = None
	
		for door in self.doors:

			if door.button is buttonPressed:
				chosenDoor = door
		
		return chosenDoor
	
	# get the item related to the key
	def getItemByButton(self, buttonPressed):

		chosenItem = None
	
		for item in self.items:

			if item.button is buttonPressed:
				chosenItem = item
		
		return chosenItem
	
	# remove an item from the list of available items
	def removeItem(self, itemToRemove):
		
		self.items.remove(itemToRemove)
