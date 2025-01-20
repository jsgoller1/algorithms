from typing import List

from test_framework import generic_test

"""
- In sorted array, arr[0] is smallest element 
- Rotating the array moves smallest elsewhere. 
- If arr[l] > arr[r], the smallest is somewhere in the middle. 

[9,0,1,2,3,4,5,6,7,8] 
"""


def search_smallest(A: List[int]) -> int:
    l, r = 0, len(A)-1
    if A[l] <= A[r]:
        return 0

    # if l == r, we found the only candidate
    while l < r:
        m = l + ((r-l) // 2)

        if A[m] > A[r]:
            # A[m] is definitely not the minimum element.
            l = m+1
        else:
            # A[m] <= A[r]; A[m] might be the
            # min element, but we don't know yet.
            r = m
    return l


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
