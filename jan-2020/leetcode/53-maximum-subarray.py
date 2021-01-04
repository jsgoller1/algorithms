"""
Given an integer array nums, find the contiguous subarray (containing at 
least one number) which has the largest sum and return its sum.
-------
Reattempting this after I had to look at the solution for the original.

At each idx, we have 3 options:
    - Include this idx in our existing subarray
    - Don't include this index in our existing subarray
    - Start a new subarray from this index

We aren't being asked to return the indexes, just the sum. 

max_sum = -float('inf')
csum = 0
for each value in arr:
    csum = max(val, csum + val)
    max_sum = max(csum, max_sum)
return max_sum
"""


class Solution:
    def maxSubArray(self, arr):
        max_sum = -float('inf')
        csum = 0
        for val in arr:
            csum = max(val, csum + val)
            max_sum = max(csum, max_sum)
        return max_sum


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([-2147483647], -2147483647),
        ([-3, -2, -1], -1),
        ([-3, -2, 1], 1)

    ]
    for input_args, expected in cases:
        actual = s.maxSubArray(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
