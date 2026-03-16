import random

from dfs import depth_first_search


class Maze:
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = [[1 for _ in range(num_cols)] for _ in range(num_rows)]
        self._generate()

    def dfs(self):
        path = depth_first_search(self)
        if path:
            for row, col in path:
                self.matrix[row][col] = 2

    def _generate(self):
        self.matrix[1][1] = 0
        self.matrix[0][1] = 0
        self.matrix[self.num_rows - 1][self.num_cols - 2] = 0
        self._carve(1, 1)

    def _carve(self, row: int, col: int):
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (
                1 <= new_row < self.num_rows - 1
                and 1 <= new_col < self.num_cols - 1
                and self.matrix[new_row][new_col] == 1
            ):

                self.matrix[row + dr // 2][col + dc // 2] = 0
                self.matrix[new_row][new_col] = 0
                self._carve(new_row, new_col)

    def __str__(self):
        string = ""
        for row in self.matrix:
            for cell in row:
                match cell:
                    case 1:
                        string += "# "
                    case 2:
                        string += "\033[32m- \033[0m"
                    case _:
                        string += "  "
            string += "\n"
        return string
