import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)

"""
init: pivot = 6, [6,2,6,7,4,3,6,8,6]
l=0, m=1, r=-1
[2,6,6,7,4,3,6,8,6], A[m] < pivot, swap l and m, inc both
l=1, m=2, r=-1
[2,6,6,7,4,3,6,8,6], A[m] = 6, inc m
l=1, m=3, r=-1
[2,6,6,6,4,3,6,8,7] A[m] = 6, inc m
l=1, m=4, r=-1
[2,4,6,6,6,3,6,8,7], A[m] =4, swap l and m, inc both
l=2, m=5, r-1
[2,4,3,6,6,6,6,8,7], A[m]=3, swap l and m, inc both
"""

def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    if len(A) < 2: 
        return A
    l, m, r, pivot = 0, 0, len(A)-1, A[pivot_index]
    while m <= r: 
        if A[m] < pivot: 
            A[l], A[m] = A[m], A[l]
            l, m = l+1, m+1
        elif A[m] == pivot:
            m += 1
        else: # A[m] > pivot
            A[m], A[r] = A[r], A[m]
            r -= 1     
    return


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure('Some elements are missing from original array')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
