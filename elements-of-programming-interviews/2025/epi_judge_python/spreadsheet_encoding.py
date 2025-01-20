from test_framework import generic_test

"""
How does this differ from normal base conversion? (no zeroes)

A = 1 
Z = 26 
AA = 27 (not A0) -> 1 col + 1*26 cols 
"""

from string import ascii_uppercase

CHAR_TO_INT = {c: i+1 for i, c in enumerate(ascii_uppercase)}

def ss_decode_col_id(col: str) -> int:
    col_id = 0
    place = 1
    for c in col[::-1]:
        col_id += CHAR_TO_INT[c] * place 
        place *= 26
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
