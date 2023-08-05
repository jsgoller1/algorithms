import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates_first(A: List[int]) -> int:
    i = 1
    target = 1
    while i < len(A):
        if A[i-1] != A[i]:
            A[target] = A[i]
            target += 1
        i += 1
    return target


def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0
    unique = 0
    curr = 1
    while (curr < len(A)):
        if A[curr] != A[unique]:
            unique += 1
            A[unique] = A[curr]
        curr += 1
    return unique + 1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
