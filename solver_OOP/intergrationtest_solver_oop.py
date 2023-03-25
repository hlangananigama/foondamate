from solver_oop import LinearEquationSolver


def test_linear_equation_solver():
    # Test case 1
    equation = "2x + 3 = 5x - 2"
    expected_solution = "x = 5/3"
    solver = LinearEquationSolver(equation)
    solution = solver.solve()
    assert solution.strip() == expected_solution

    # Test case 2
    equation = "3x = 9 + 2x"
    expected_solution = "x = 9"
    solver = LinearEquationSolver(equation)
    solution = solver.solve()
    assert solution.strip() == expected_solution

    # Test case 3
    equation = "3x + 5 = 2x + 9"
    expected_solution = "x = 4"
    solver = LinearEquationSolver(equation)
    solution = solver.solve()
    assert solution.strip() == expected_solution

    # Test case 4
    equation = "3x + 6 = 3x + 9"
    expected_solution = "There is no x value to solve for - there is no solution!"
    solver = LinearEquationSolver(equation)
    solution = solver.solve()
    assert solution.strip() == expected_solution

    # Test case 5
    equation = "5(x + 2) = 3x + 10"
    expected_solution = "There is no x value to solve for - there is no solution!"
    solver = LinearEquationSolver(equation)
    solution = solver.solve()
    assert solution.strip() == expected_solution


if __name__ == '__main__':
    test_linear_equation_solver()
    print(f"All Integration Test Cases Passed!\n\n")
