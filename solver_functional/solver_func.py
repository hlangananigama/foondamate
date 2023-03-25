import argparse
import sympy


def rearrange_equation(equation):
    # Split the equation string at the equals sign

    print(f"This is the starting equation:\n\n{equation}\n\n")

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
            f"Move everything to one side (preferrably the LHS) and cancel out like terms to simplify as follows:\n\n{simplified_equation_str.replace('*', '')}\n\n")
        # print(simplified_equation_str)

        return simplified_equation_str

    except (ValueError, TypeError, AttributeError, SyntaxError):
        print("Invalid equation format. Please make sure the equation is of the correct format and try again.")
        print("Example: '4(2x + 2) = -4x + 13'")
        exit()
    # Implementation of rearrange_equation function


def move_constants_right(equation_str):
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
        f"The next step is to move the constant to the right, keep x value on the left side:\n\n{new_equation.replace('*', '')}\n\n")
    # print(new_equation)
    return new_equation
    # Implementation of move_constants_right function


def final_solution(rearranged_eq):

    # Move constants to the right-hand side
    new_eq = move_constants_right(rearranged_eq)

    # Parse the left-hand side expression using sympy
    lhs_expr = sympy.sympify(new_eq.split('=')[0].strip())

    # Get the coefficient of 'x' and the constant on the right-hand side
    x_coeff = lhs_expr.coeff('x')
    const = sympy.sympify(new_eq.split('=')[1].strip())

    # Solve for 'x' by dividing coefficient of 'x' with the constant
    x = const/x_coeff

    # Format the solution as a string
    x_str = 'x = {}'.format(x)

    print(f"Divide the right side with the coefficient of x:\n\n")

    # print(f"finally, the solution:\n x = ")

    return x_str


def solve_equation(equation):
    # Rearrange equation to isolate variable on left-hand side
    rearranged_eq = rearrange_equation(equation)

    if 'x' in rearranged_eq:

        if len(rearranged_eq.split()) == 5:

            x_str = final_solution(rearranged_eq)

        else:

            return f"x needs to be zero for the expression to be true:\n\nSolution : x = 0"

    else:

        return "There is no x value to solve for - there is no solution!"

        # Return the solution and the final equation
    return f"{x_str}\n\n"


def main():
    # Define command line arguments
    parser = argparse.ArgumentParser(description='Solve a linear equation')
    parser.add_argument('equation', type=str, help='the equation to solve')

    # Parse command line arguments
    args = parser.parse_args()

    # Solve the equation
    solution = solve_equation(args.equation)

    # Print the solution
    print(solution)


if __name__ == '__main__':
    main()
