from classes.game import Game
from classes.constants import Constants
from classes.score import Score

class Simulation:
    def __init__(self):
        self.quantity = Constants.SIMULATIONS_QUANTITY
        self.winner = ['', 0]
        self.play_games()
        self.output_time_out()
        self.output_average()
        self.output_percentage()
        self.output_winner()

    def play_games(self):
        for _ in range(self.quantity):
            Game()

    def output_time_out(self):
        print(Constants.OUTPUT_TIME_OUT)
        print(Score.time_out)

    def output_average(self):
        print(Constants.OUTPUT_AVERAGE)
        print(f'{Score.rounds/self.quantity:.2f}')

    def output_percentage(self):
        print(Constants.OUTPUT_PERCENTAGE)
        for p in Score.players:
            print(f'{p}: {Score.players[p]/self.quantity:.2f}')

    def output_winner(self):
        print(Constants.OUTPUT_WINNER)
        for p in Score.players:
            self.winner = [p, Score.players[p]]
        print(self.winner[0])