import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
[2,4,6,3,5,7]
[1,2,3,4,5,6]
"""

def even_odd_first(A: List[int]) -> None:
    i, j = 0, len(A)-1
    while i < j:
        if A[i] % 2 == 0:
            i += 1
            continue 
        if A[j] % 2:
            j -= 1 
            continue
        if A[i] % 2 and A[j] % 2 == 0:
            A[i], A[j] = A[j], A[i]
            i, j = i+1, j-1
    return

def even_odd(A):
    l, r = 0, len(A)-1
    while l < r:
        if not (A[l] % 2 and (A[r] % 2 == 0)): # If the condition we need for swapping is false
            l += 0 if A[l] % 2 else 1          # increment l if A[l] is even
            r -= 1 if A[r] % 2 else 0          # decrement r if A[r] is odd 
        else:
            A[l], A[r] = A[r], A[l]            # Otherwise, swap and continue 

@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
