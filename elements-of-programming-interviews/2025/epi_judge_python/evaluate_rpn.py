from test_framework import generic_test

"""
Cases:
- empty / expression
- single number: 1234
- basic expression: 1 1 +
- recursive expression: 2 2 + 1 1 + + 

("10,5,-,2,2,+,+", 9)
 -> 
 [+,+,-], [2,2,5,10]
 [+,+], [2,2,5]

"""

OPS = {
    "+": lambda x, y: x + y, 
    "*": lambda x, y: x * y, 
    "/": lambda x, y: x // y, 
    "-": lambda x, y: x - y
}


# doesn't work due to recursive depth
def recurse(symbols):
    if not symbols:
        return 0
    symbol = symbols.pop()
    if symbol in OPS:
        op2 = recurse(symbols)
        op1 = recurse(symbols)
        return OPS[symbol](op1, op2)
    return int(symbol)

def evaluate(expression: str) -> int:
    if not expression:
        return 0 
    symbols = [(sym if sym in OPS else int(sym)) for sym in expression.split(",")]
    stack = []
    for sym in symbols:
        if isinstance(sym, int):
            stack.append(sym)
        else:
            op2, op1 = stack.pop(), stack.pop()
            stack.append(OPS[sym](op1, op2))
    return stack[0]

"""
for expr, total in [
    ("", 0),
    ("1234", 1234),
    ("10,5,-", 5), 
    ("10,5,-,2,2,+,+", 9),
    ("10,10,10,+,-", -10),
    ("10,10,10,10,+,+,+", 40)
]:
    actual = evaluate(expr)
    assert actual == total, f"{expr}: {actual} != {total}"
    print("----")

"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
