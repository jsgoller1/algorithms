import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


"""
Suppose i < j < k
If arr[j] > j, we know that every subsequent arr[k] > k, so no candidates are there. 
If arr[j] > j, we know nothing about arr[i] and i, unless the array is contiguous (which it isn't)

If arr[j] < j, then this is also true for every arr[i] and i, but we know nothing about arr[k] and k.

So do a standard binary search but:
    if arr[mid] > mid: pick lower
    if arr[mid] == mid, that's our answer.
    if arr[mid] < mid, pick higher.
"""


def search_entry_equal_to_its_index(arr: List[int]) -> int:
    l, r = 0, len(arr)-1
    while l <= r:
        mid = l + ((r-l) // 2)
        if arr[mid] > mid:
            r = mid - 1
        elif arr[mid] == mid:
            return mid
        else:  # arr[mid] < mid
            l = mid + 1
    return -1


@enable_executor_hook
def search_entry_equal_to_its_index_wrapper(executor, A):
    result = executor.run(functools.partial(search_entry_equal_to_its_index,
                                            A))
    if result != -1:
        if A[result] != result:
            raise TestFailure('Entry does not equal to its index')
    else:
        if any(i == a for i, a in enumerate(A)):
            raise TestFailure('There are entries which equal to its index')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_entry_equal_to_index.py',
            'search_entry_equal_to_index.tsv',
            search_entry_equal_to_its_index_wrapper))
