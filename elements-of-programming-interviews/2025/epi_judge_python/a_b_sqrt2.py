from typing import List

from test_framework import generic_test
import math
from heapq import heappush, heappop

def generate_first_k_a_b_sqrt2(k: int) -> List[float]:
    if not k:
        return []
    visited, minheap, stack = set(), [], [(0,0)]
    while stack:
        a,b = stack.pop()
        val = a + b * math.sqrt(2)
        heappush(minheap, -val)
        popped = None
        if len(minheap) > k:
            popped = heappop(minheap)
        if popped == -val:
            # Don't explore further if the largest element from the heap is the one we just put in
            continue
        for child in [(a+1, b), (a, b+1)]:
            if child not in visited:
                visited.add(child)
                stack.append(child)
    return [-val for val in sorted(minheap, reverse=True)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('a_b_sqrt2.py', 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
