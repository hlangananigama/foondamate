# Equation Solver

This is an implementation of an equation solver that takes a linear-first order equation as input (type string data type) and outputs a maximum of five steps on how to approach the solution.

There is both an Object Oriented Programming (OOP) implementation of the solution, as well as a functional approach. Both produce the same steps and results. The file names are descriptive and should make it easy to identify which one is which.

## How to run

1. Open your terminal (MacOS) and clone the repository onto the directory you would like to work in.
2. Change directory into the folder that was just cloned.
3. Change directory into OOP folder: `cd solver_OOP`
4. Paste or type the following command on the CLI: `python solver_oop.py "2(4x + 3) + 6 = 24 - 4x"`
5. To run the unit test and integration test files, use the same command as step 3, but replace `solver_oop.py` with `unittest_solver_oop.py` or `intergrationtest_solver_oop.py`. No need for an equation input for tests!

Error handling is included to explain what is wrong if the input is not in the correct format (missing quotation marks, for example).

Student creativity is always encouraged, and this is only one way (not the only way) to approach the problem. Here are the steps in the solution approach:

1.  Print the equation that needs to be solved so that it is clear if there were any mistakes and the solution is not mistaken for that of another equation. Do not forget to change the sign when moving something across the "=" sign.

    - Assume this is the starting equation:

             "5(2x + 24x + 19) = 2x + 22"

2.  Simplify the expression. Move everything to one side to eliminate or cancel out like terms by performing basic arithmetic (addition and subtraction). The left-hand-side (LHS) is usually easier to work with. You end up with something that looks like this:

                    128x + 73 = 0

3.  This step only runs if there is a value for `x` to solve for and a constant (i.e., the solution is non-zero). Move the constant of the simplified expression to the RHS and keep the `x`-coefficient positive by multiplying by -1 if negative. Do not forget to change the sign when moving something across the "=" sign.

                        128x = -73

4.  This step also only runs if there is both an `x` to solve for and a constant. The solution is straightforward from here onwards - simply divide the coefficient on the RHS by the `x` value on the LHS.

                        x = -73/128

5.  This step returns the solution and always runs - even if steps 3 and 4 did not run. Possible solutions:

    - For the example problem, the solution would be as follows: the RHS expression would be evaluated if possible (i.e., to give an integer solution), otherwise, the fraction remains, which may be the same expression as that in step 4.

                     x = -73/128`

    - If there is no `x` variable to solve for, the solution would be:

             "There is no `x` value to solve for -
                     there is no solution!"

    - The solution if there is no constant means `x` needs to be zero for the whole expression to be true, so it would return the following:
      `x` needs to be zero for the expression to be true.
      Solution: `x = 0`
