import unittest
from solver_func import rearrange_equation, move_constants_right, solve_equation


class TestRearrangeEquation(unittest.TestCase):
    def test_rearrange_equation(self):
        equation = "3(4x + 3) + 6 = 24 -2x"
        result = rearrange_equation(equation)
        expected_result = "14*x - 9 = 0"
        self.assertEqual(result, expected_result)


class TestMoveConstantsRight(unittest.TestCase):
    def test_move_constants_right(self):
        equation_str = "43*x - 9 = 0"
        result = move_constants_right(equation_str)
        expected_result = "43*x = 9"
        self.assertEqual(result, expected_result)


class TestSolveEquation(unittest.TestCase):
    def test_solve_equation(self):
        equation = "3(4x + 3) + 6 = 24 -4x"
        result = solve_equation(equation)
        expected_result = "x = 9/16"
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
