import random

class Random_Player:
    def __init__(self):
        pass

    def choose_move(self, valid_moves: dict) -> tuple:
        return random.choice(list(valid_moves.keys()))