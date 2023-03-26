import unittest
from solver_func import solve_equation


class TestSolveEquationIntegration(unittest.TestCase):
    def test_solve_equation(self):
        # Test case 1
        equation = "2x + 3 = 11"
        expected_result = "x = 4"
        result = solve_equation(equation)
        self.assertEqual(result, expected_result)

        # Test case 2
        equation = "3x - 7 = 5x + 9"
        expected_result = "x = -8"
        result = solve_equation(equation)
        self.assertEqual(result, expected_result)

        # Test case 3
        equation = "4(2x - 1) + 2x = 10 - 2(3x + 1)"
        expected_result = "x = 3/4"
        result = solve_equation(equation)
        self.assertEqual(result, expected_result)

        # Test case 4
        equation = "7x + 3 = 3(2x + 5) - 4"
        expected_result = "x = 8"
        result = solve_equation(equation)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
