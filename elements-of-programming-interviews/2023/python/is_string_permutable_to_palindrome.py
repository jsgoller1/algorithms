from test_framework import generic_test


"""
in: string
out: bool

edges: 
    - empty (assume yes)
    - case? assuming it matters, "Aba" not palindrome
    - whitespace? assume words won't have whitespace, can handle if so

count letters?
"""
from collections import Counter


def can_form_palindrome(s: str) -> bool:
    return len([v for v in Counter(s).values() if v % 2]) < 2


if __name__ == '__main__':
    assert can_form_palindrome("")
    assert can_form_palindrome("aa")
    assert can_form_palindrome("Aaa")
    assert not can_form_palindrome("ba")
    assert not can_form_palindrome("john says no")
    assert not can_form_palindrome("sit on a potato pan otis")
    assert can_form_palindrome("sitonapotatopanotis")

    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
