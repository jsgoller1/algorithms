from typing import List

from test_framework import generic_test, test_utils

"""
brute force: nlogk, just k largest with a separate heap

largest is A[0]. Is children are at 2*0 + 1 and 2*0 + 2
heap property is that parents are always gt than children
so if we do a level order traversal, we can get largest elements as long as we look
at every item on a level; this is tricky though - could see some edge cases we don't want.

maybe a recursive function? push elements to min heap; if current idx is larger, then append or pop
and explore children?

cases:
- empty, singleton, duplicates?
- heap unbalanced?
"""

from heapq import heappush, heappop

def k_largest_in_binary_heap(A: List[int], k: int) -> List[int]:
    out = []
    def recurse(idx):
        if idx >= len(A):
            return 
        if len(out) < k or out[0] < A[idx]:
            heappush(out, A[idx])
            if len(out) > k: 
                heappop(out)
            recurse(2*idx+1)
            recurse(2*idx+2)

    recurse(0)
    return out 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'k_largest_in_heap.py',
            'k_largest_in_heap.tsv',
            k_largest_in_binary_heap,
            comparator=test_utils.unordered_compare))
