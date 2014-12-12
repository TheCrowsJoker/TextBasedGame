class Door(object):
    def __init__(self, button, name, leadsTo, requiredItem = None):
        self.button = button
        self.name = name
        self.leadsTo = leadsTo
        self.requiredItem = requiredItem
