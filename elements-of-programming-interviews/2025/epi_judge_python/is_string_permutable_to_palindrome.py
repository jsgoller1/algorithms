from test_framework import generic_test

from collections import Counter

def can_form_palindrome(s: str) -> bool:
    letters = Counter(s)
    found_odd = False 
    for count in letters.values():
        if count % 2:
            if found_odd:
                return False 
            else:
                found_odd = True 
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
