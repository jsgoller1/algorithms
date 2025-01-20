from test_framework import generic_test

"""
Input: string (could be large, but fits in mem)
Output: int (same constraints; represents string)

- "" invalid
- A = 1, Z = 26
- AA = 1*(26^0) + 1*(26*1)
- No 0, no negatives
"""
import string

DIGITS = {c: i+1 for i, c in enumerate(string.ascii_uppercase)}


def ss_decode_col_id(col: str) -> int:
    total = 0
    place = 1
    for c in col[::-1]:
        total += (DIGITS[c] * place)
        place *= 26
    return total


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
