import os

from sudokutools.generate import generate
from sudokutools.solve import bruteforce

if __name__ == '__main__':

    out = open("sudoku4.csv", "w+")

    for _ in range(100):
        sudoku = generate(size=(2, 2))
        out.write(sudoku.encode())
        print(sudoku.encode(), end="")
        # print("")
        # print(sudoku)

        for solution in bruteforce(sudoku):
            # print("")
            # print(solution)
            # print("")
            out.write(";")
            out.write(solution.encode())
            print(";", end="")
            print(solution.encode(), end="")

        out.write("\n")
        print("")

    out.close()
