from test_framework import generic_test

from collections import Counter
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    required_chars = Counter(letter_text)
    have_chars = Counter(magazine_text)
    for c in required_chars:
        if required_chars[c] > have_chars[c]:
            return False 
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
