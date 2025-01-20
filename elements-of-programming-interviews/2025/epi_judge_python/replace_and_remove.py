import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


'''
delete b and replace a with dd
abac. -> ddddc
    aac..
    aac.c
    aaddc
    ddccc


- if every char in array is occupied, we might still be able to replace a with dd if we have enough b to delete 

brute force: 
- 1 pass to delete b / squeeze 
- 2 pointer pass from reverse to replace with dd
- 1 pass to rearrange shift string to beginning 

'''

def delete_b(size, s):
    i = j = 0 
    while j < size:
        if s[j] == 'b':
            s[j] = ''
        else:
            s[i] = s[j]
            i += 1
        j += 1
    return i-1

def replace_a(last_i, s):
    l, r = last_i, len(s)-1
    while 0 <= l: 
        if s[l] == 'a':
            s[r], s[r-1] = 'd', 'd'
            r-=2 
        else:
            s[r] = s[l]
            r-=1 
        l-=1 
    return r+1

def left_shift(first_i, s):
    l, r = 0, first_i
    while r < len(s):
        s[l] = s[r]
        l,r = l+1, r+1 
    return l

def replace_and_remove(size: int, s: List[str]) -> int:
    last_i = delete_b(size, s)
    first_i = replace_a(last_i, s)
    last_i = left_shift(first_i, s)
    return last_i


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
