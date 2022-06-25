import random

class Dice:
    min = 1
    max = 6
    
    def roll():
        """Return a dice side from 1 to 6."""
        return random.randint(Dice.min, Dice.max)
    
    def tendency():
        """Return a random dice tendency."""
        sum = 0

        for _ in range(Dice.max):
            sum += Dice.roll()
        return sum/Dice.max
