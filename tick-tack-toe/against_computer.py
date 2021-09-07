import ast
import time

import numpy as np
import random


class Game():
    def __init__(self):
        self.matrix = np.ndarray(shape=(3, 3), dtype=object)
        self.coords_list = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        self.human = 1
        self.computer = 2
        self.any_won = False

    def is_win(self, point):
        if np.all(self.matrix[0] == point) or np.all(self.matrix[1] == point) or np.all(self.matrix[2] == point):
            return True
        elif np.all(self.matrix.T[0] == point) or np.all(self.matrix.T[1] == point) or np.all(
                self.matrix.T[2] == point):
            return True
        elif np.all(self.matrix.diagonal() == point) or np.all(np.fliplr(self.matrix).diagonal() == point):
            return True
        else:
            return False

    def play_game(self):
        player = self.human
        print("Let's start!")
        while len(self.coords_list) > 0:
            try:
                print(self.matrix)
                print(f"Available coordinates for choosing: {self.coords_list}")
                print()

                if player == self.human:
                    coords = ast.literal_eval(input(f"Player - {player}, take a shot please: "))
                    point = self.matrix[coords[0] - 1][coords[1] - 1] = 0
                else:
                    print("Computer is thinking...")
                    time.sleep(3)
                    coords = random.choice(self.coords_list)
                    print(f"Computer has chosen {coords} coords")
                    point = self.matrix[coords[0] - 1][coords[1] - 1] = 'X'
                self.coords_list.remove(coords)

                self.any_won = self.is_win(point)
                if self.any_won:
                    return f"Congratulations! Player - {player} has won."
                player = self.computer if player == self.human else self.human

            except SyntaxError:
                print("Unexpected symbols input")
            except ValueError:
                print("Coords are not in the coords-list")
            except IndexError:
                print(f"Index {coords[0]} out of range")
                player = player


matrix = Game()
print(matrix.play_game())











