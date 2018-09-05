import re

"""
Statement: https://leetcode.com/problems/different-ways-to-add-parentheses/description/

I solved this during my Bradfield class; I did the SUPER heuristic over Slack and on a whiteboard
before implementing it.
"""

OPERATORS = ['+', '-', '*']


class Solution:
    def diffWaysToCompute(self, input_str):
        return wrapper(input_str)


def solve(expr):
    """
    solve()
    - 'break' expression on an operator
    - recursively fork each sub expression
    - combine results
    """
    if len(expr) == 1:
        return expr
    elif len(expr) == 3:
        expr = ''.join(expr)
        return [str(eval(expr))]
    elif (len(expr) % 2) == 0:
        raise ValueError("Valid expressions must be of odd length.")

    combinations = []
    for i, symbol in enumerate(expr):
        if symbol in OPERATORS:
            left_expr = solve(expr[:i])
            right_expr = solve(expr[i+1:])
            op = expr[i]
            combinations += combine(left_expr, right_expr, op)
    return combinations


def combine(l_arr, r_arr, op):
    combinations = []
    for l_operand in l_arr:
        for r_operand in r_arr:
            combinations.append(str(eval(l_operand + op + r_operand)))
    return combinations


def wrapper(expr):
    symbols = re.split("([-+*])", expr)
    solution = solve(symbols)
    return [int(val) for val in solution]


if __name__ == '__main__':
    s = Solution()
    assert s.diffWaysToCompute("2-1-1") == [2, 0]
