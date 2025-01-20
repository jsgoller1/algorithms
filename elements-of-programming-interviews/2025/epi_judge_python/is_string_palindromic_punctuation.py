from test_framework import generic_test

from string import ascii_letters, digits

ALPHANUMERIC = set(ascii_letters) | set(digits)

def is_palindrome(s: str) -> bool:
    s = s.lower()
    l, r = 0, len(s)-1
    while l < r: 
        if s[l] not in ALPHANUMERIC:
            l += 1 
        elif s[r] not in ALPHANUMERIC:
            r -= 1
        else:
            if s[l] != s[r]:
                return False
            l, r = l+1, r-1 
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
