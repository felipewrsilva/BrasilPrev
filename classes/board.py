from classes.house import House
from classes.constants import Constants

class Board:
    def __init__(self):
        self.properties = []
        self.set_properties()
        self.sum = 0
    
    def set_properties(self):
        for position in range(Constants.HOUSES):
            property = House(position + 1)
            self.properties.append(property)

    def get_properties(self):
        for p in self.properties:
            self.sum += p.rent_cost
            print(f'{p.position:02d} - {p.sale_cost:06.2f} - {p.rent_cost:05.2f}')
        