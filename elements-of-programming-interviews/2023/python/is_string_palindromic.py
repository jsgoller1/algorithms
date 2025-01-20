from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    if not s:
        return False
    l = 0
    r = len(s)-1
    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
