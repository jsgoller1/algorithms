from test_framework import generic_test


def divide(x, y):
    if (x < y or y == 0):
        return 0
    amount = 1
    quotient = 0
    while x > y:
        y <<= 1
        amount <<= 1
    while x:
        if x >= y:
            x -= y
            quotient += amount
        else:
            y >>= 1
            amount >>= 1
    return quotient


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_divide.py',
                                       'primitive_divide.tsv', divide))
