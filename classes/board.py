from house import House
from constants import Constants

class Board:
    def __init__(self):
        self.properties = []
        self.set_properties()
    
    def set_properties(self):
        for position in range(Constants.QUANTITY):
            property = House(position + 1)
            self.properties.append(property)

    def get_properties(self):
        for property in self.properties:
            print(property.position, end=' ')
        