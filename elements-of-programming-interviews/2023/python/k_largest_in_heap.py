from typing import List

from test_framework import generic_test, test_utils

"""
- In max heap, root is largest, and they only get smaller. 
- Leaves of item at i are at 2**i, 2**i+1
- If one child is greater than the other, we can't explore the lesser until we explore the best ones
- Could we use a heap for this? 
    - each time we evaluate a node, put it into set of largest, and heappush all children.
    - heappop to get next node. 
    - Do this k many times; always ensures that of children, we get the biggest. 
"""

from collections import namedtuple
from heapq import heappush, heappop

entry = namedtuple("entry", ["val", "idx"])


def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    if (not A) or (len(A) <= k):
        return A
    largest = []
    heap = [entry(-A[0], 0)]
    while len(largest) < k:
        curr = heappop(heap)
        largest.append(-curr.val)
        left_idx, right_idx = 2*curr.idx+1, (2*curr.idx)+2
        if left_idx < len(A):
            heappush(heap, entry(-A[left_idx], left_idx))
        if right_idx < len(A):
            heappush(heap, entry(-A[right_idx], right_idx))
    return largest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
