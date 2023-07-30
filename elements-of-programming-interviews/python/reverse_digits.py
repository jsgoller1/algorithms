from test_framework import generic_test


def reverse(x: int) -> int:
    y = 0
    neg = -1 if x < 0 else 1
    x *= neg
    while x:
        y *= 10
        y += x % 10
        x = int(x/10)
    return y * neg


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
