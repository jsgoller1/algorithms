from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    out = m + n - 1
    m, n = m-1, n-1 
    while m > -1 and n > -1: 
        if A[m] >= B[n]:
            A[out] = A[m]
            m -= 1
        else:
            A[out] = B[n]
            n -= 1
        out -= 1 

    while m > -1:
        A[out] = A[m]
        m -= 1
        out -= 1

    while n > -1:
        A[out] = B[n]
        n -= 1
        out -= 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
