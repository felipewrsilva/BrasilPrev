import random
from classes.board import Board
from classes.dice import Dice
from classes.player import *
from classes.score import Score

class Game:
    def __init__(self):
        self.status = True
        self.board = self.config_board()
        self.players = self.config_players()
        random.shuffle(self.players)
        self.start()
        self.finish()

    def config_board(self):
        return Board().houses

    def config_players(self):
        return [Cautious(), Demanding(), Impulsive(), Random()]
    
    def start(self):
        rounds = Constants.MAX_ROUNDS
        for round in range(rounds):
            for player in self.players:
                if (self.status):
                    self.round(player)
                else:
                    Score.rounds += round + 1
                    if (round == 0):
                        Score.one_round += 1
                    return
        Score.time_out += 1
        Score.rounds += rounds + 1
    
    def finish(self):
        for player in self.players:
            if (player.playing):
                Score.players[player.type] += 1
                return

    def round(self, player):
        if (player.playing == False):
            return
        self.set_new_position(player)
        self.buy_or_rent(player)
        self.check_player_balance(player)

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
        self.check_game_ended()
        self.release_houses(player)

    def check_game_ended(self):
        count_players_playing = 0
        for player in self.players:
            if (player.playing == True):
                count_players_playing += 1
        if count_players_playing == 1:
            self.status = False

    def release_houses(self, player):
        for house in self.board:
            if(house.owner == player):
                house.owner = None