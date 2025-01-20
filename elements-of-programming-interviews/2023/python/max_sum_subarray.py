from typing import List

from test_framework import generic_test

"""
Some cases:
[1,2,3,4,-4,5]
[1,2,3,4,-4,-3,-2,-1,5]
[1,2,3,4,-4,-3,-2,5,5]

brute force: check every subarray 
o(n): at each element, we either "start from here, or include in original array"
"""


def find_maximum_subarray(A: List[int]) -> int:
    # Assuming empty subarray is valid selection and equals 0
    best = 0
    rsum = 0
    for val in A:
        rsum = max(rsum+val, val)
        best = max(rsum, best)
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_sum_subarray.py',
                                       'max_sum_subarray.tsv',
                                       find_maximum_subarray))
