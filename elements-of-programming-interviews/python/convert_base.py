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

# easier to read than ord()/chr()
CHAR_AS_NUM = {str(i): i for i in range(10)} | {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
NUM_AS_CHAR = "0123456789ABCDEF"


def to_new_base(num: int, b2: int) -> str:
    if num == 0:
        return "0"
    val = ""
    while num:
        remainder = num % b2
        val = NUM_AS_CHAR[remainder] + val   # prepend the new digit
        num //= b2
    return val


def to_base_ten(num_as_string: str, b1: int) -> int:
    total = 0
    place = 1
    for c in num_as_string[::-1]:
        total += (CHAR_AS_NUM[c] * place)
        place *= b1
    return total


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    if not num_as_string:
        return ""
    neg = num_as_string[0] == '-'
    num_as_string = num_as_string[1:] if neg else num_as_string

    num_base_10 = to_base_ten(num_as_string, b1)
    num_b2 = to_new_base(num_base_10, b2)

    return ("-" if neg else "") + num_b2


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
