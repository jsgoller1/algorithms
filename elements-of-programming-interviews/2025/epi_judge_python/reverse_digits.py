from test_framework import generic_test


def reverse(x: int) -> int:
    new = 0 
    neg = x < 0
    x = abs(x)
    while x: 
        new *= 10
        new += x % 10 
        x //= 10
    return new * (-1 if neg else 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
