import unittest
from solver_oop import LinearEquationSolver


class TestLinearEquationSolver(unittest.TestCase):

    def test_rearrange_equation(self):
        solver = LinearEquationSolver("2x + 3 = 5x - 2")
        rearranged_eq = solver.rearrange_equation()
        self.assertEqual(rearranged_eq, "5 - 3*x = 0")

    def test_move_constants_right(self):
        solver = LinearEquationSolver("3x = 9 + 2x")
        rearranged_eq = solver.rearrange_equation()
        new_eq = solver.move_constants_right(rearranged_eq)
        self.assertEqual(new_eq, "x = 9")

    def test_solve(self):
        solver = LinearEquationSolver("3x + 5 = 2x + 9")
        solution = solver.solve()
        self.assertEqual(solution, "x = 4\n\n")

        solver = LinearEquationSolver("3x + 6 = 3x + 9")
        solution = solver.solve()
        self.assertEqual(
            solution, "There is no x value to solve for - there is no solution!\n\n")

        solver = LinearEquationSolver("2x + 4 = 2x + 8")
        solution = solver.solve()
        self.assertEqual(
            solution, "There is no x value to solve for - there is no solution!\n\n")


if __name__ == '__main__':
    unittest.main()
    print(f"All Unit Test Cases Passed!\n\n")
