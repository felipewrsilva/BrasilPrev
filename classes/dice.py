import random
from classes.constants import Constants

class Dice:
    def roll():
        """Return a dice side from 1 to 6."""
        return random.randint(Constants.DICE_MIN, Constants.DICE_MAX)
    