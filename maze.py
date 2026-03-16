class Maze:
    def __init__(self, num_rows: int, num_cols: int):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.matrix = [[1 for _ in range(num_cols)] for _ in range(num_rows)]

    def __str__(self):
        string = ""
        for row in self.matrix:
            for cell in row:
                if cell == 1:
                    string += "# "
                else:
                    string += "  "
            string += "\n"
        return string
