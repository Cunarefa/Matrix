import ast
import random
import time
from typing import List, Tuple
import itertools

import numpy as np


class Player():
    def __init__(self, player):
        self.player = player


class Matrix():
    def __init__(self, size: tuple):
        self.size = size
        self.counter = 0
        self.matrix = np.ndarray(shape=self.size, dtype=object)

    def __next__(self, array):
        if self.counter < self.size[0] or self.counter < self.size[1]:
            self.counter += 1
            return array[self.counter - 1]
        else:
            raise StopIteration

    def __iter__(self):
        return self


class Game():
    def __init__(self, desk_size: Tuple, players: List):
        self.desk_size = desk_size
        self.desk = np.ndarray(shape=self.desk_size, dtype=object)
        self.players = players
        self.any_won = False

    def is_win(self, point):
        if np.all(self.desk[0] == point) or np.all(self.desk[1] == point) or np.all(self.desk[2] == point):
            return True
        elif np.all(self.desk.T[0] == point) or np.all(self.desk.T[1] == point) or np.all(
                self.desk.T[2] == point):
            return True
        elif np.all(self.desk.diagonal() == point) or np.all(np.fliplr(self.desk).diagonal() == point):
            return True
        else:
            return False

    def play_game(self):
        coords_list = list(itertools.product(range(1, self.desk_size[0] + 1), range(1, self.desk_size[1] + 1)))
        player = random.choice(self.players)
        while np.all([i for i in self.desk]) is None:
            try:
                print(F"Player {player} is moving \n")

                if player == 'computer':
                    print("Computer is thinking...")
                    time.sleep(2)
                    coords = random.choice(coords_list)
                    print(f"Computer has chosen {coords} coords")
                else:
                    coords = ast.literal_eval(input(f"Player - {player}, take a shot please: "))

                point = self.desk[coords[0] - 1][coords[1] - 1] = self.players.index(player) + 1
                coords_list.remove(coords)

                self.any_won = self.is_win(point)
                if self.any_won:
                    return f"Congratulations! Player - {player} has won."

                player = self.change_player(player)

            except ValueError as err:
                print(err)
                player = player

        return "Game over. Have no winner"

    def change_player(self, player):
        player_index = self.players.index(player)
        player = self.players[0] if self.players[player_index] == self.players[-1] else self.players[player_index + 1]
        return player


f = Game((3, 3), ['John', 'computer'])
print(f.play_game())
#
# f = itertools.product(range(3), range(3))
# print([i for i in f])









