from classes.constants import Constants
import random


class House:
    def __init__(self):
        self.sale_cost = self.get_sale_cost()
        self.rent_cost = self.get_rent_cost()
        self.owner = None
    
    def get_sale_cost(self):
        return random.randint(Constants.SALE_COST_MIN, Constants.SALE_COST_MAX)

    def get_rent_cost(self):
        return self.sale_cost * Constants.RENT_PERCENT
    
    def buy(self, owner):
        self.owner = owner
        owner.balance = owner.balance - self.sale_cost
    
    def rent(self, owner):
        owner.balance = owner.balance - self.rent_cost
        if (self.owner != None):
            self.owner.balance += self.rent_cost
        