from test_framework import generic_test


# Palindrome reads forward and backward the same way,
# so just reverse and compare; can do this a few ways.

def is_palindrome_number_simple(x: int) -> bool:
    if x < 0:
        return False
    return str(x)[::-1] == str(x)


def is_palindrome_number(x: int) -> bool:
    """
    If the interviewer says "no conversion to string",
    then just compute the reversed decimal value and
    compare to the original.
    """
    if x < 0:
        return False
    original = x
    rev_x = 0
    while (x):
        rev_x *= 10
        rev_x += x % 10
        x = x//10
    return original == rev_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
