from test_framework import generic_test
from test_framework.test_failure import TestFailure

char_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
int_to_char = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
               5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def int_to_string(x: int) -> str:
    if x == 0:
        return '0'
    chars = []
    neg = False
    if x < 0:
        neg = True
        x *= -1
    while x:
        chars.append((int_to_char[x % 10]))
        x = x // 10
    return (''.join(chars + (['-'] if neg else [])))[::-1]


def string_to_int(s: str) -> int:
    total = 0
    place = 1
    for char in reversed(s):
        if char == '-':
            total *= -1
        elif char == '+':
            pass
        else:
            total += (char_to_int[char] * place)
        place *= 10
    return total


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
