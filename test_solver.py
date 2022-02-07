import csv
import unittest

from parameterized import parameterized

from solver import Solver
# from my_solver import MySolver


def load_game_data():
    with open("./sudoku.csv") as data_file:
        data = [line for line in csv.reader(data_file, delimiter=";")]

    return data


def custom_name_func(testcase_func, _param_num, param):
    return "%s for ['%s' -> %s]" % (
        testcase_func.__name__,
        parameterized.to_safe_name(param.args[0]),
        parameterized.to_safe_name(param.args[1])
        )


class SolverTestCase(unittest.TestCase):

    @parameterized.expand(load_game_data, testcase_func_name=custom_name_func)
    def test_game_data(self, sudoku, solution):
        s = Solver.solve(sudoku)
        # s = MySolver.solve(sudoku)
        self.assertEqual(solution, s)

    def test_sudoku_one(self):
        s = Solver.solve(
            "700900000600030000000070100002000459000000600800004000025008010008300040060702500")
        self.assertEqual(
            "751946823684231975239875164312687459547193682896524731925468317178359246463712598", s)


if __name__ == '__main__':
    unittest.main()
