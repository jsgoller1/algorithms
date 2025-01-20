import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def pivot_sort(A, left, test_fn):
    curr = left
    while curr < len(A):
        if test_fn(A[curr]):
            tmp = A[left]
            A[left] = A[curr]
            A[curr] = tmp
            left += 1
        curr += 1
    return left


def dutch_flag_partition(pivot_index: int, A: List[int]) -> None:
    val = A[pivot_index]
    left = pivot_sort(A, 0, lambda x: x < val)
    pivot_sort(A, left, lambda x: x == val)
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
    import random
    arr = [random.randint(-100, 100) for _ in range(100)]
    partition = 20
    print(f"Partitioning on {arr[partition]}")
    dutch_flag_partition(partition, arr)
    print(arr)
    """
    exit(
        generic_test.generic_test_main('dutch_national_flag.py',
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
    """
