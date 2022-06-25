from classes.constants import Constants
from classes.dice import Dice
import random

rent_percent = random.randint(50, 100) / 100

class House:
    def __init__(self, position):
        self.position = position
        self.sale_cost = self.get_sale_cost()
        self.rent_cost = self.get_rent_cost()
        self.owner = None
    
    def get_sale_cost(self):
        return Constants.INITIAL_MONEY / (Constants.HOUSES - (self.position - 1)) / Dice.tendency()

    def get_rent_cost(self):
        return self.sale_cost * rent_percent