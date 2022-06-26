import random
from classes.constants import Constants

class Player:
    def __init__(self, type):
        self.balance = Constants.INITIAL_BALANCE
        self.type = type
        self.playing = True
        self.position = 0
    
    def buy_or_rent(self, house, decision):
        if(decision):
            house.buy(self)
            return True
        else:
            house.rent(self)
            return False

class Cautious(Player):
    def __init__(self):
        super().__init__(Constants.PLAYER_CAUTIOUS)
        
    def buy_or_rent(self, house):
        decision = False
        after_buy = self.balance - house.sale_cost
        if(after_buy > Constants.PLAYER_CAUTIOUS_CONDITION):
            decision = True
        return super().buy_or_rent(house, decision)

class Demanding(Player):
    def __init__(self):
        super().__init__(Constants.PLAYER_DEMANDING)
        
    def buy_or_rent(self, house):
        decision = False
        if(house.rent_cost > Constants.PLAYER_DEMANDING_CONDITION):
            decision = True
        return super().buy_or_rent(house, decision)

class Impulsive(Player):
    def __init__(self):
        super().__init__(Constants.PLAYER_IMPULSIVE)
        
    def buy_or_rent(self, house):
        decision = True
        return super().buy_or_rent(house, decision)

class Random(Player):
    def __init__(self):
        super().__init__(Constants.PLAYER_RANDOM)

    def buy_or_rent(self, house):
        decision = random.choice([True, False])
        return super().buy_or_rent(house, decision)