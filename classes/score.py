from classes.constants import Constants
from classes.player import Demanding, Impulsive

class Score:
    players = {
        Constants.PLAYER_CAUTIOUS: 0,
        Constants.PLAYER_DEMANDING: 0,
        Constants.PLAYER_IMPULSIVE: 0,
        Constants.PLAYER_RANDOM: 0
    }
    time_out = 0
    one_round = 0
    rounds = 0
