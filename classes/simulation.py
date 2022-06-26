from classes.game import Game
from classes.constants import Constants
from classes.score import Score

class Simulation:
    def __init__(self):
        quantity = Constants.SIMULATIONS_QUANTITY
        for _ in range(quantity):
            Game()
        print(Constants.OUTPUT_TIME_OUT)
        print(Score.time_out)
        print(Constants.OUTPUT_AVERAGE)
        print(f'{Score.rounds/quantity:.2f}')
        print(Constants.OUTPUT_PERCENTAGE)
        winner = ['', 0]
        players = Score.players
        for p in players:
            print(f'{p}: {players[p]/quantity:.2f}')
            winner = [p, players[p]]
        print(Constants.OUTPUT_WINNER)
        print(winner[0])
