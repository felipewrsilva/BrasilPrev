from classes.board import Board
from classes.player import *
from classes.dice import Dice
import random

class Game:
    def __init__(self):
        self.board = self.config_board()
        self.players = self.config_players()
        random.shuffle(self.players)
        self.round()

    def config_board(self):
        return Board().houses

    def config_players(self):
        return [Cautious(), Demanding(), Impulsive(), Random()]
    
    def round(self):
        for player in self.players:
            self.set_new_position(player)
            self.check_player_balance(player)
            print(player.type, player.balance)

    def buy_or_rent(self, player):
            house = self.board[player.position]
            player.buy_or_rent(house)

    def set_new_position(self, player):
        new_position = player.position + Dice.roll()
        if(new_position >= Constants.HOUSES):
            player.position = new_position - Constants.HOUSES
        else:
            player.position = new_position

    def check_player_balance(self, player):
        if(player.balance < 0):
            player.playing = False
        self.release_houses(player)

    def release_houses(self, player):
        for house in self.board:
            if(house.owner == player):
                house.owner = None