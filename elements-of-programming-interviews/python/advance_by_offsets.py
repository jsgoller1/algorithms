from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    best = A[0]
    curr = 0
    for dist in A:
        if (curr > best):
            return False
        if (best >= len(A)-1):
            return True
        best = max(curr + A[curr], best)
        curr += 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
