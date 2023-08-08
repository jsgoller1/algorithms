from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    if not x:
        return "0"
    neg = "-" if x < 0 else ""
    x = x*-1 if neg else x
    string = []
    while x:
        string.append(str(x % 10))
        x //= 10
    return neg + "".join(string[::-1])


def string_to_int(s: str) -> int:
    place = 1
    val = 0
    neg = s[0] == "-"
    s = s[1:] if neg or s[0] == "+" else s
    for char in s[::-1]:
        val += int(char) * place
        place *= 10
    return val * -1 if neg else val


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    # print(int_to_string(0))
    # print(string_to_int("0"))
    # """
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
    # """
