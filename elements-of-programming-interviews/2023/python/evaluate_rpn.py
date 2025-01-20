from test_framework import generic_test


OPERATIONS = ["*", "+", "/", "-"]


def apply(operation, op1, op2):
    if operation == "*":
        return op1 * op2
    elif operation == "+":
        return op1+op2
    elif operation == "/":
        return op1 // op2
    else:
        return op1 - op2


def evaluate(expression: str) -> int:
    # NOTE: assuming valid expression
    if not expression:
        return 0
    stack = []
    expr = expression.split(",")
    for val in expr:
        if val not in OPERATIONS:
            stack.append(int(val))
        else:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(apply(val, op1, op2))
    return stack.pop()


if __name__ == '__main__':
    """
    cases = [
        ("0", 0),
        ("", 0),
        ("4", 4),
        ("-4", -4),
        ("4,4,+", 8),
        ("10,10,X,4,4,+,+,2,/", 54)

    ]
    for expression, expected in cases:
        assert evaluate(expression) == expected, f"{evaluate(expression)} != {expected}"
    """
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
