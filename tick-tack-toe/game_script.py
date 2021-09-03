import ast

import numpy as np


class Game():
    def __init__(self):
        self.matrix = np.ndarray(shape=(3, 3), dtype=object)
        self.coords_list = [(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
        self.player_1 = 1
        self.player_2 = 2
        self.any_won = False

    def play_game(self):
        player = self.player_1
        print("Let's start!")
        while len(self.coords_list) > 0:
            try:
                print(self.matrix)
                print(f"Available coordinates for choosing: {self.coords_list}")
                print()

                coords = ast.literal_eval(input(f"Player - {player}, take a shot please: "))
                if player is self.player_1:
                    point = self.matrix[coords[0] - 1][coords[1] - 1] = 0
                else:
                    point = self.matrix[coords[0] - 1][coords[1] - 1] = 'X'
                self.coords_list.remove(coords)

                self.any_won = self.is_win(point)
                if self.any_won:
                    return f"Congratulations! Player - {player} has won."

                player = self.player_2 if player == self.player_1 else self.player_1
            except SyntaxError:
                print("Unexpected symbols input")
            except ValueError:
                print("Coords are not in the coords-list")
            except IndexError:
                print(f"Index {coords[0]} out of range")
                player = player

        return "Game over. Have no winner"

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


matrix = Game()
print(matrix.play_game())

