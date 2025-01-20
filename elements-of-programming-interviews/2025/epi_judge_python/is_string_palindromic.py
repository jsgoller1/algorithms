from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
