from test_framework import generic_test

"""
every even char is at y = 0
in the odd chars, every even-odd char is at 1, and every odd-odd is at -1. However,
let's say even-odds are at -1 and odd-odds are at 1, so even-odds come first. 

So:
first pass, insert (0, idx, c) in array for all evens
second pass, map even-odds to (-1, idx, c) and odd-odds to (1, idx, c)
then sort (if needed) and reconstruct string 
"""

def evens(arr_len):
    for i in range(arr_len):
        if not i % 2:
            yield i 

def odds(arr_len, get_subarr_evens):
    is_even = get_subarr_evens
    for i in range(arr_len):
        if i % 2:
            if is_even:
                yield i 
            is_even = not is_even

def snake_string(s: str) -> str:
    chars = [s[i] for i in odds(len(s), True)] + \
            [s[i] for i in evens(len(s))] + \
            [s[i] for i in odds(len(s), False)]
    return ''.join(chars)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('snake_string.py', 'snake_string.tsv',
                                       snake_string))
