from typing import Iterator, List

from test_framework import generic_test

from heapq import heappop, heappush

"""
cases:
- empty
- singleton
- duplicates (all duplicates)
- perfectly sorted
"""

def sort_approximately_sorted_array(sequence: Iterator[int],
                                    k: int) -> List[int]:
    out, heap = [], []
    for val in sequence:
        heappush(heap, val)
        if len(heap) > k:
            out.append(heappop(heap))
    while heap:
        out.append(heappop(heap))
    return out 


def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'sort_almost_sorted_array.py', 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
