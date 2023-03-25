import argparse
import sympy


class LinearEquationSolver:
    def __init__(self, equation):
        self.equation = equation

    def rearrange_equation(self):

        equation = self.equation

        if "*" in equation:
            print(
                f"\n\nDo not put the multiplication sign. Here is an example: '4x(2 + 3) = 3 + 23x'\n\n")
            exit()

        print(f"\n\n1. This is the starting equation:\n\n   {equation}\n\n")

        lhs, rhs = equation.split('=')

        # Strip any whitespace from the left-hand and right-hand sides
        lhs = lhs.strip()
        rhs = rhs.strip()

        # Add multiplication sign before any opening bracket
        lhs = lhs.replace('(', '*(')
        rhs = rhs.replace('(', '*(')

        # Replace 'x' with '*x' for left and right-hand sides
        lhs = lhs.replace('x', '*x')
        rhs = rhs.replace('x', '*x')

        try:
            # Parse the left-hand side expression using sympy
            lhs_expr = sympy.sympify(lhs)

            # Rearrange the equation to isolate 'x' on the left-hand side
            rearranged_expr = lhs_expr - sympy.sympify(rhs)

            # Simplify the rearranged equation using sympy
            simplified_expr = sympy.simplify(rearranged_expr)

            # Convert the expression back to a string
            simplified_equation = str(simplified_expr)

            simplified_equation_str = str(simplified_equation) + ' = 0'

            # add something here to print

            print(
                f"2. Move everything to one side (preferrably the LHS) and cancel out like terms to simplify as follows:\n\n   {simplified_equation_str.replace('*', '')}\n\n")
            # print(simplified_equation_str)

            return simplified_equation_str

        except (ValueError, TypeError, AttributeError, SyntaxError):
            print(
                "Invalid equation format. Please make sure the equation is of the correct format and try again.")
            print("Example: '4(2x + 2) = -4x + 13'")
            exit()
        # Implementation of rearrange_equation function

    def move_constants_right(self, equation_str):
        # Split the equation string at the equals sign
        equation_list = equation_str.split()

        # Strip any whitespace from the left-hand and right-hand sides
        lhs = equation_list[0].strip()
        const = equation_list[2].strip()

        # Get the constant value on the right-hand side
        sign = equation_list[1]

        # Check the sign and change it if necessary
        if equation_list[1] == '+':
            RHS = '-' + equation_list[2]
        else:
            RHS = equation_list[2]

        # Create the new equation string with 'x' on the left and constant on the right

        new_equation = lhs + ' = ' + RHS

        if 'x' not in lhs:

            # print(f"Move x and coeffecient to the LHS; if x coeff is negative, multiply by -1 on both sides to make x coefficient positive:\n\n{new_equation.replace('*', '')}\n\n")

            new_equation = RHS + ' = ' + lhs

        print(
            f"3. The next step is to move the constant to the right, keep x value on the left side:\n\n   {new_equation.replace('*', '')}\n\n")
        # print(new_equation)
        return new_equation
        # Implementation of move_constants_right function

    def solve(self):
        # Rearrange equation to isolate variable on left-hand side
        rearranged_eq = self.rearrange_equation()
        # new_eq = self.move_constants_right(rearranged_eq)

        if 'x' in rearranged_eq:

            if len(rearranged_eq.split()) == 5:

                # x_str = final_solution(rearranged_eq)

                # new_eq = move_constants_right(rearranged_eq)

                new_eq = self.move_constants_right(rearranged_eq)

                # Parse the left-hand side expression using sympy
                lhs_expr = sympy.sympify(new_eq.split('=')[0].strip())

                # Get the coefficient of 'x' and the constant on the right-hand side
                x_coeff = lhs_expr.coeff('x')
                const = sympy.sympify(new_eq.split('=')[1].strip())

                # Solve for 'x' by dividing coefficient of 'x' with the constant
                x = const/x_coeff

                # Format the solution as a string
                x_str = 'x = {}'.format(x)

                print(
                    f"4. Divide the right side with the coefficient of x:\n\n   x = {const}/{x_coeff}\n\n")

            else:

                return f"x needs to be zero for the expression to be true:\n\n  Solution : x = 0\n\n"

        else:

            return "There is no x value to solve for - there is no solution!\n\n"

            # Return the solution and the final equation
        return f"{x_str}\n\n"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Linear Equation Solver')
    parser.add_argument('equation', type=str, help='Equation to solve')
    args = parser.parse_args()

    solver = LinearEquationSolver(args.equation)
    solution = solver.solve()
    print(
        f"5. The solution to the equation '{args.equation}' is:\n\n   {solution}")
