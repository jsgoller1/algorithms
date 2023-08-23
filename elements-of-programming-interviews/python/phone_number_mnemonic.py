from typing import List

from test_framework import generic_test, test_utils


KEYPAD = {
    "2": "ABC",
    "3": "DEF",
    "4": "GHI",
    "5": "JKL",
    "6": "MNO",
    "7": "PQRS",
    "8": "TUV",
    "9": "WXYZ",
}


def phone_mnemonic(phone_number: str) -> List[str]:
    solutions = []

    def process_digit(phone_number, i, base):
        if i == len(phone_number):
            solutions.append("".join(base))
            return
        if phone_number[i] in ["0", "1"]:
            process_digit(phone_number, i+1, base + [phone_number[i]])
        else:
            new_chars = KEYPAD[phone_number[i]]
            for char in new_chars:
                process_digit(phone_number, i+1, base + [char])

    process_digit(phone_number, 0, [])
    return solutions


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
