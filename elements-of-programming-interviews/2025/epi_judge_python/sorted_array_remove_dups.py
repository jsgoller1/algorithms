import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
[1,1,2,3,3,3]
[1,2,2,3,3,3]
[1,2,3,3,3,3]

[1,2,3,4,5]

two idxes, i = 0, j = 1
- everything left of i is unique, j is the current place in the array
- if i == j, j++
- if j =! i, i++, A[i] = A[j] =
"""

# Returns the number of valid entries after deletion.
def delete_duplicates(A: List[int]) -> int:
    if len(A) < 2:
        return len(A)
    count = 1 
    i,j= 0, 1
    while j < len(A):
        if A[i] == A[j]:
            j += 1
        else:
            i += 1
            A[i] = A[j]
            count += 1
    return count 

for arr, expected, count in [
    ([1], [1], 1),
    ([1,1,2,2,3,3], [1,2,3], 3),
    ([1,2,3,4,5], [1,2,3,4,5], 5)
]:
    old = arr[:]
    new_count = delete_duplicates(arr)
    assert count == new_count, f"{old} -> {arr}, {count} != {new_count}"
    for i in range(count):
        assert arr[i] == expected[i], f"{old}: {arr} != {expected}"


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))