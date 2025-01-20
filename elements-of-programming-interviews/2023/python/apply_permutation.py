from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i, idx in enumerate(perm):
        if idx == -1:
            continue
        val = A[idx]
        nextIdx = perm[idx]
        while nextIdx != -1:
            nextVal = A[nextIdx]
            A[nextIdx] = val
            val = nextVal
            perm[idx] = -1
            idx = nextIdx
            nextIdx = perm[idx]
    return


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
