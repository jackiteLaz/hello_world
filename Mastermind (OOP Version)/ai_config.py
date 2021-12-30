from random import randint
from game_rules import Game


class Ai:
    def __init__(self):
        self.__solution = []

    def populate(self):
        game = Game()
        for i in range(4):
            self.__solution.append(game.get_color_dict()[game.get_color_abv()[randint(0, 4)]])

    def get_solution(self):
        return self.__solution
