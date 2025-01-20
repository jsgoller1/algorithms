from test_framework import generic_test

"""
execute as two separate conversions: to base 10 and from it. 
"""

CHAR_TO_INT = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A':10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
INT_TO_CHAR = {v: k for k,v in CHAR_TO_INT.items()}

def to_base_ten_int(string, b1):
    base_ten_int = 0 
    for i, c in enumerate(reversed(string)):
        base_ten_int += CHAR_TO_INT[c] * b1**i
    return base_ten_int

def from_base_ten_int(base10int, b2):
    new_base_int = []
    while base10int:
        new_base_int.append(INT_TO_CHAR[base10int % b2])
        base10int //= b2 
    return ''.join(reversed(new_base_int)) if new_base_int else '0'

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    neg = num_as_string[0] == '-'
    num_as_string = num_as_string[1:] if neg else num_as_string
    return ('-' if neg else '') + from_base_ten_int(to_base_ten_int(num_as_string, b1), b2)
"""
actual = from_base_ten_int(10205, 16)
expected = hex(10205)[2:]
assert actual == expected, f"{actual} != {expected}"

"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
