import random
class Constants:
    HOUSES = 20
    MAX_ROUNDS = 1000
    SIMULATIONS_QUANTITY = 300
    TIME_OUT = 'time_out'
    ONE_ROUND = 'one_round'
    ROUNDS = 'rounds'

    DICE_MIN = 1
    DICE_MAX = 6
    
    SALE_COST_MIN = 10
    SALE_COST_MAX = 1000
    RENT_PERCENT_MIN = 50
    RENT_PERCENT_MAX = 100
    RENT_PERCENT = random.randint(RENT_PERCENT_MIN, RENT_PERCENT_MAX) / 100
    
    INITIAL_BALANCE = 300
    PLAYER_CAUTIOUS = 'Cautious'
    PLAYER_IMPULSIVE = 'Impulsive'
    PLAYER_RANDOM = 'Random'
    PLAYER_DEMANDING = 'Demanding'
    PLAYER_CAUTIOUS_CONDITION = 80
    PLAYER_DEMANDING_CONDITION = 50

    OUTPUT_TIME_OUT = 'Quantas partidas terminam por time out (1000 rodadas)'
    OUTPUT_AVERAGE = 'Quantos turnos em média demora uma partida'
    OUTPUT_PERCENTAGE = 'Qual a porcentagem de vitórias por comportamento dos jogadores'
    OUTPUT_WINNER = 'Qual o comportamento que mais vence'