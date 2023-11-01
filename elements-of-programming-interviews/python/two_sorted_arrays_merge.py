from typing import List

from test_framework import generic_test


def merge_two_sorted_arrays(A: List[int], m: int, B: List[int],
                            n: int) -> None:
    new_arr = []
    i = j = 0
    while i < m and j < n:
        if A[i] <= B[j]:
            new_arr.append(A[i])
            i += 1
        else:
            new_arr.append(B[j])
            j += 1

    while i < m:
        new_arr.append(A[i])
        i += 1
    while j < n:
        new_arr.append(B[j])
        j += 1

    i = 0
    while i < m+n:
        A[i] = new_arr[i]
        i += 1

    return


def merge_two_sorted_arrays_wrapper(A, m, B, n):
    merge_two_sorted_arrays(A, m, B, n)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sorted_arrays_merge.py',
                                       'two_sorted_arrays_merge.tsv',
                                       merge_two_sorted_arrays_wrapper))
