from typing import List

from test_framework import generic_test

import heapq


def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    heap = [(arr[0], 0, i) for i, arr in enumerate(sorted_arrays) if arr]
    heapq.heapify(heap)
    merged = []
    while heap:
        val, idx, arr_id = heapq.heappop(heap)
        merged.append(val)
        new_idx = idx+1
        parent_arr = sorted_arrays[arr_id]
        if new_idx < len(parent_arr):
            heapq.heappush(heap, (parent_arr[new_idx], new_idx, arr_id))

    return merged


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
