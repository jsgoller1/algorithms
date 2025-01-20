from test_framework import generic_test

"""
- Bases can be between 2 and 16
- Can be empty? 
- Can exceed integer limits (not issue for python)
- Negatives
- num_as_string[0] is most sig fig
- 0 and 1 are always valid; A = 10, ..., F = 15

Input: string representing num in b1
Output: string representing num in b2

- Ex: convert "12345" to int 12345
    - add each digit, then multiply total by 10. 
"""
import functools
import string

NUM_AS_CHAR = "0123456789ABCDEF"


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # Assuming 2 <= b1,b2 <= 16
    if num_as_string in ["", "0"]:
        return num_as_string
    neg = num_as_string[0] == "-"

    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[neg:], 0)

    def recurse(num_as_int, b2):
        if num_as_int == 0:
            return ""
        remainder = num_as_int % b2
        return recurse(num_as_int // b2, b2) + NUM_AS_CHAR[remainder]

    return ("-" if neg else "") + recurse(num_as_int, b2)


if __name__ == '__main__':
    print(convert_base("1234", 10, 5))
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
