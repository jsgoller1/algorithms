"""
- expressions always valid
- operators: ('+', '-', '*', '/')
- all ints nonnegative, no parens
- L to r evaluation with a stack? 
    - push - and + whenever we find them
    - if we see any * or /, get next element, combine, push.
    - then do second pass and combine + and -
    - ends with 1 item on stack, return it. 
    - all expressions valid, so will always have following element. 

----
got all tests except last one, TLE, at 35:00
"""
import cProfile
import string
from massive_test_case import massive_expr


def tokenize_to_stack(s):
    if not s:
        return set(), []

    tokens = []
    token = ""
    operations = set()
    for c in s:
        if c in ["+", "-", "/", "*"]:
            operations.add(c)
            tokens.append(token)
            tokens.append(c)
            token = ""
        elif c in string.digits:
            token += c

    # Append final
    tokens.append(token)
    return operations, tokens


def apply_mult_div(tokens):
    reduced = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token in ["*", "/"]:
            op1 = int(reduced.pop())
            op2 = int(tokens[i+1])
            result = str(op1 // op2) if token == "/" else str(op1 * op2)
            reduced.append(result)
            i += 2
        else:
            reduced.append(token)
            i += 1
    return reduced


def apply_add_sub(tokens):
    if len(tokens) < 3:
        return tokens

    l, op, r = 0, 1, 2
    while len(tokens) != 1:
        op1 = int(tokens[l])
        op2 = int(tokens[r])
        tokens[l] = str(op1 + op2) if tokens[op] == "+" else str(op1 - op2)
        del tokens[1]
        del tokens[1]
    return tokens


class Solution:
    def calculate(self, s: str) -> int:
        operations, tokens = tokenize_to_stack(s)
        if "/" in operations or "*" in operations:
            tokens = apply_mult_div(tokens)
        if "+" in operations or "-" in operations:
            tokens = apply_add_sub(tokens)
        return int(tokens[0])


assert tokenize_to_stack("") == (set(), [])
assert tokenize_to_stack("1") == (set(), ["1"])
assert tokenize_to_stack("3+2*2") == (set(["+", "*"]), ["3", "+", "2", "*", "2"])
assert tokenize_to_stack("3/2") == (set(["/"]), ["3", "/", "2"])
assert tokenize_to_stack(" 3+5 / 2 ") == (set(["+", "/"]), ["3", "+", "5", "/", "2"])

assert apply_mult_div([]) == []
assert apply_mult_div(["3", "/", "2"]) == ["1"]
assert apply_mult_div(["3", "*", "2"]) == ["6"]
assert apply_mult_div(["3", "*", "2", "+", "55"]) == ["6", "+", "55"]
assert apply_mult_div(["3", "*", "2", "/", "2"]) == ["3"]

assert apply_add_sub(["3"]) == ["3"]
assert apply_add_sub(["3", "+", "0"]) == ["3"]
assert apply_add_sub(["3", "+", "0", "-", "3"]) == ["0"]

s = Solution()
cases = [
    # ("1", 1),
    # ("3+2*2", 7),
    # ("3/2", 1),
    # (" 3+5 / 2 ", 5),
    # ("0-1-1-1-1-1", -5),
    # ("0-1-1-1-1-1*100", -104),
    # ("    0-1 -1-1-   1    -1*100     ", -104),
    (massive_expr, 2)
]
for expr, expected in cases:
    cProfile.run('s.calculate(expr)')
    # actual = s.calculate(expr)
    # assert actual == expected, f"{expr}: {actual} == {expected}"
