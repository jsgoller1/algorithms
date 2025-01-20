from typing import List

from test_framework import generic_test

"""
cases:
- empty
- single element
- all decreasing, all increasing
- every other increases and decreases
"""

from collections import deque
from heapq import heappop, heappush

def construct_arrs(arr):
    if not arr:
        return []
    out, curr = [], []
    i = 0 
    increasing = True 
    while i < len(arr)-1:
        curr.append(arr[i])
        # detect flip
        if (arr[i] > arr[i+1]) if increasing else (arr[i] < arr[i+1]):
            out.append(curr if increasing else curr[::-1])
            curr = []
            increasing = not increasing
        i += 1 
    if curr:
        out.append(curr if increasing else curr[::-1])
    return out + [[arr[i]]] # simple hack, technically will return k + 1 arrays, but won't affect complexity

def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:
    heap = []
    out = []
    for arr in construct_arrs(A):
        heappush(heap, deque(arr))
    while heap:
        arr = heappop(heap)
        out.append(arr.popleft())
        if arr:
            heappush(heap, arr)
    return out 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sort_increasing_decreasing_array.py',
                                       'sort_increasing_decreasing_array.tsv',
                                       sort_k_increasing_decreasing_array))