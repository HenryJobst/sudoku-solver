from math import isqrt

SPACE_COUNT_PER_CELL = 3


class MySolver:

    def __init__(self, sudoku):
        box_dim = self.calculate_box_dim(sudoku)
        self.dim = box_dim * box_dim
        self.grid = [[{x+1 for x in range(self.dim)} for _ in range(self.dim)] for _ in range(self.dim)]
        self.box_dim = box_dim
        self.apply(sudoku)

    def create_line(self) -> str:
        result = ""
        for i in range(self.dim * SPACE_COUNT_PER_CELL + self.box_dim + 1):
            result += "-"

        return result

    def format(self, compact=False) -> str:
        result = ""

        if not compact:
            result += "\n"
            result += self.create_line()
        for row in range(self.dim):
            if not compact:
                result += "\n|"
            for col in range(self.dim):
                if not compact:
                    result += " "
                cell = self.grid[row][col]
                if compact:
                    if len(cell) == 1:
                        result += next(iter(cell))
                    else:
                        result += "0"
                else:
                    if len(cell) == 1:
                        result += next(iter(cell))
                    else:
                        result += " "
                if not compact:
                    result += " "
                if not compact and (col+1) % self.box_dim == 0:
                    result += "|"
            if not compact and (row + 1) % self.box_dim == 0:
                result += "\n" + self.create_line()
        return result

    def encode(self) -> str:
        return self.format(compact=True)

    def apply(self, sudoku: str) -> None:
        for c in range(self.dim):
            colu = sudoku[c*self.dim:c*self.dim+self.dim]
            for r in range(self.dim):
                number = colu[r]
                if number != "0":
                    self.grid[c][r] = {number}

    def calculate_box_dim(self, sudoku: str) -> int:
        return isqrt(isqrt(len(sudoku)))

    @staticmethod
    def solve(sudoku: str) -> str:
        solver = MySolver(sudoku)
        print(solver.format())
        return solver.encode()
