from classes.house import House
from classes.constants import Constants

class Board:
    def __init__(self):
        self.houses = []
        self.set_houses()
        self.sum = 0
    
    def set_houses(self):
        for _ in range(Constants.HOUSES):
            house = House()
            self.houses.append(house)

    def get_houses(self):
        for p in self.houses:
            self.sum += p.rent_cost
            print(f'{p.position:02d} - {p.sale_cost:06.2f} - {p.rent_cost:05.2f}')
    
    