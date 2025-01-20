from typing import List

from test_framework import generic_test

from heapq import heappush, heappop

"""
cases: no elements, single elements, duplicates in list
just push all to heap and pop? minheap so sorted order implicit (* -1 otherise) - nlogn
arrays are already sorted though, really only need top of each? still nlogn possibly
"""

from collections import deque

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = []
    out = []
    for array in sorted_arrays:
        heappush(heap, deque(array))
    while heap:
        arr = heappop(heap)
        out.append(arr.popleft())
        if arr:
            heappush(heap, arr)
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
