from typing import List

from test_framework import generic_test

"""
the min point's preceding element is greater than it
Cases:
- array is already sorted
- min point is somewhere in the middle
- min point is the final element 

when we get the midpoint, if it's smaller than l, exclude right half
if it's greater than r, exclude left half 

"""

def search_smallest(A: List[int]) -> int:
    l, r = 0, len(A)-1 
    if A[l] <= A[r]:
        return l

    while l+1 < r:
        m = (l + r) // 2
        if A[m] < A[l]:
            r = m 
        else:
            l = m 
    return r if A[l] > A[r] else l

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
