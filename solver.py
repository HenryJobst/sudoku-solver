from sudokutools.solve import bruteforce
from sudokutools.sudoku import Sudoku


class Solver:

    @staticmethod
    def solve(sudoku: str) -> str:
        sudoku_decoded = Sudoku.decode(sudoku)
        for solution in bruteforce(sudoku_decoded):
            sudoku_solved_encoded = solution.encode()
            return sudoku_solved_encoded
