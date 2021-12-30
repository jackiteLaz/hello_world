from random import randint

import board
from board import Row


class Game:
    def __init__(self):
        self.__color_dict = {"k": "black",
                             "w": "white",
                             "g": "green",
                             "r": "red",
                             "b": "blue",
                             "y": "yellow"}
        self.__color_abv = ["k", "w", "g", "r", "b", "y"]
        self.__color_report = {
            "black": 0,
            "white": 0,
            "green": 0,
            "red": 0,
            "blue": 0,
            "yellow": 0
        }
        self.__attempt_color_report = {
            "black": 0,
            "white": 0,
            "green": 0,
            "red": 0,
            "blue": 0,
            "yellow": 0
        }
        self.__solution = []
        self.__attempt = []
        self.__red_score = 0
        self.__white_score = 0
        self.__round = 1  # check if necessary
        # game initialization
        self.board = board.Board()
        self.populate_solution()

    def __str__(self):
        return "The colors are: White(w) Black(k) Green(g) Red(r) Blue(b) Yellow(y)"

    def get_red_score(self):
        return self.__red_score

    def get_white_score(self):
        return self.__white_score

    def get_color_dict(self):
        return self.__color_dict

    def get_color_abv(self):
        return self.__color_abv

    def get_solution(self):
        return self.__solution

    def get_attempt(self):
        return self.__attempt

    def populate_solution(self):
        if input("PvP or PvE? ").upper() == "PVE":  # setup for AI
            self.__solution = list(self.__color_dict.get(self.__color_abv[randint(0, 5)]) for _ in range(5))
        else:
            self.__solution = list(self.__color_dict.get(input("Enter the color of pin #" + str(x) + ": ")) for x in range(1, 6))
        self.populate_color_report()
        print(self.__solution)

    def populate_attempt(self):
        print(self)
        self.__attempt = list(input("Enter the color of pin #" + str(x) + ": ") for x in range(1, 6))
        self.populate_attempt_color_report()
        print(self.__attempt, "is the attempt.")

    def populate_color_report(self):
        for i in self.__solution:
            self.__color_report[i] += 1

    def populate_attempt_color_report(self):
        for i in self.__attempt:
            self.__attempt_color_report[i] += 1

    def check_score(self, solution, attempt):
        for i in range(4):
            if solution[i] == attempt[i]:
                self.__red_score += 1
                self.__attempt_color_report[attempt[i]] -= 1
        for i in range(4):
            if self.__attempt_color_report[self.__color_dict[self.__color_abv[i]]] > 0 and self.__color_report[self.__color_dict][self.__color_abv[i]]:
                self.__white_score += min([self.__attempt_color_report[self.__color_dict[self.__color_abv[i]]], self.__color_report[self.__color_dict][self.__color_abv[i]]])
        self.board.set_row(self.__attempt, self.__red_score, self.__white_score)

    def transfer_to_board(self):  # check if necessary
        return Row(self.__attempt, self.__red_score, self.__white_score)
