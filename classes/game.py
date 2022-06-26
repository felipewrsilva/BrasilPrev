from classes.board import Board
from classes.player import *
from classes.dice import Dice

class Game:
    def __init__(self):
        self.board = self.config_board()
        self.players = self.config_players()
        random.shuffle(self.players)

    def config_board(self):
        return Board()
    
    def config_players(self):
        return [Cautious(), Demanding(), Impulsive(), Random()]
    
    def round(self):
        for player in self.players:
            new_position = player.position + (Dice.roll() - 1)
            if(new_position >= Constants.HOUSES):
                player.position = new_position - Constants.HOUSES
            else:
                player.position = new_position
            self.check_buy(player)
    
    def check_buy(self, player):
        house = self.board[player.position]
        player.buy(house)

    
    def check_players(self, player):
        player.playing = False
        self.release_houses(player)