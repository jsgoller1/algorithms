from test_framework import generic_test
import collections
import string


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter = collections.Counter(letter_text)
    magazine = collections.Counter(magazine_text)
    return all(letter[k] <= magazine[k] for k in letter if k not in string.whitespace)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
