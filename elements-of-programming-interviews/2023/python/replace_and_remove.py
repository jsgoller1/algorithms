import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


"""
input: size (int), list of strings
output: int, size of new list? (assume so for now)
Can assume sufficient size (lists aren't immutable anyway)

Edge cases:
- empty string
- no b's or a's
- all b's, all a's

Remove every b, replace every a with 2 ds
- Trivial: O(n) storage, write to new string
- Better if we can use O(c) storage
- can't do forward pass, deletes characters we've not yet examined 
- can safely assume enough space for final result

- if we first delete every b, we have just a string with chars and ds, 
  should give pretty wide margin (may not, though)
  - worst edge case: array is 12 a's with 24 spaces; but I don't think
    it could catch up unless there wasn't enough room

plan (3 O(n) passes):
- delete b's and downshift; 
- definitely will have space starting at right end; start from last character for a replacement
- then do a pass to downshift 
"""

import string


def delete_bs(size: int, s: List[str]) -> int:
    j = 0
    i = 0
    while i < size:
        if s[i] != 'b':
            s[j] = s[i]
            j += 1
        i += 1
    return j


def reversed_replace(size: int, s: List[str]) -> int:
    i, j = size-1, len(s)-1
    while i >= 0:
        if s[i] != 'a' and s[i] not in string.whitespace:
            s[j] = s[i]
            j -= 1
        else:
            s[j] = 'd'
            j -= 1
            s[j] = 'd'
            j -= 1
        i -= 1
        # print(f"{i}: {s}")
    return j+1


def leftshift(start: int, s: List[str]):
    i = 0
    while start < len(s):
        s[i] = s[start]
        i += 1
        start += 1
    return i


def replace_and_remove(size: int, s: List[str]) -> int:
    # print(f"size: {size}")
    new_size = delete_bs(size, s)
    new_start = reversed_replace(new_size, s)
    # print(f"new start: {new_start}")
    new_size = leftshift(new_start, s)
    return new_size


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    """
    # s = ["a", "b", "a", "b", "a", "b", "a", "b", "", "", "", "", "", "", ""]
    # print(replace_and_remove(8, s))
    # print(s)
    """
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
