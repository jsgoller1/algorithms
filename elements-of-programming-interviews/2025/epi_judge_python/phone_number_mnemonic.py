from typing import List

from test_framework import generic_test, test_utils

"""
Book doesn't specify, so for 0 and 1 we will just directly insert them into the string.
Assuming e
"""

num_to_chars = {
    '0': "0",
    '1': "1",
    '2': "ABC",
    '3': "DEF",
    '4': "GHI",
    '5': "JKL",
    '6': "MNO",
    '7': "PQRS",
    '8': "TUV",
    '9': "WXYZ"
}

def phone_mnemonic(phone_number: str) -> List[str]:
    solution = []
    def recurse(chars, idx):
        if idx == len(phone_number):
            solution.append(''.join(chars)) 
            return
        for trans_char in num_to_chars[phone_number[idx]]:
            chars.append(trans_char)
            recurse(chars, idx+1)
            chars.pop()
    recurse([], 0)
    return solution if phone_number else []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
