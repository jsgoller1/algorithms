from typing import List

from test_framework import generic_test

"""
Smallest case would be like:
k = 3: 0 1 0 | 1 0 | 1 0 

brute force sort is nlogn, can ideally do better 
vals could be pos, neg, or zero 

"""
import heapq
import collections

subarray = collections.namedtuple("subarray", ["val", "left", "right", "increasing"])


def get_subarrays(arr):
    if not arr or (len(arr) == 1):
        return [arr]
    subarrays = []
    curr = []
    increasing = arr[0] < arr[1]
    i = 0
    while i < len(arr)-1:
        if ((arr[i] < arr[i+1]) and not increasing) or ((arr[i] > arr[i+1]) and increasing):
            subarrays.append(curr if increasing else curr[::-1])
            curr = []
            increasing = not increasing
        curr.append(arr[i])
        i += 1

    if not curr:
        subarrays.append([arr[i]])
    else:
        curr.append(arr[i])
        subarrays.append(curr if increasing else curr[::-1])
    return subarrays


def sort_k_increasing_decreasing_array(array: List[int]) -> List[int]:
    subarrs = get_subarrays(array)
    heap = [(arr[0], 0, i) for i, arr in enumerate(subarrs)]
    heapq.heapify(heap)
    merged = []
    while heap:
        val, idx, arr_id = heapq.heappop(heap)
        merged.append(val)
        new_idx = idx+1
        parent_arr = subarrs[arr_id]
        if new_idx < len(parent_arr):
            heapq.heappush(heap, (parent_arr[new_idx], new_idx, arr_id))

    return merged


if __name__ == '__main__':
    cases = [
        # [1, 2, 3, 4, 5, 4, 3, 2, 1, 2, 3, 4, 5],
        # [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1],
        # [1, 2, 4, 4, 5, 1, 2, 3, 4, 5, -10, 10, -10],
        [2147483647, 8, 4, 2, 1, 0, -1, -2147483648]
    ]
    for case in cases:
        # print(get_subarrays(case))
        expected = sorted(case)
        actual = sort_k_increasing_decreasing_array(case)
        assert actual == expected, f"\ncase: {case}\n{actual} != {expected}"
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))
