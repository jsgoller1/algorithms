from test_framework import generic_test

# empty is palindrome
# " " is palindrome (it's also empty)


def is_palindrome(s: str) -> bool:
    l, r = 0, len(s)-1
    while l <= r:
        while l < len(s) and not s[l].isalnum():
            l += 1
        while r >= 0 and not s[r].isalnum():
            r -= 1
        if (0 <= l <= r < len(s)) and not s[l].lower() == s[r].lower():
            return False
        r -= 1
        l += 1
    return True


if __name__ == '__main__':
    assert is_palindrome("")
    assert is_palindrome(" ")
    assert is_palindrome("a")
    assert is_palindrome("aa")
    assert is_palindrome(" a a ")
    assert is_palindrome(" a     a ")
    assert not is_palindrome("ab")
    assert not is_palindrome("ab ")
    assert not is_palindrome(" ab ")
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
