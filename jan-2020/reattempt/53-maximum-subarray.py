"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Constraints:
    - 1 <= nums.length <= 2 * 10^4 (up to 20,000 numbers)
    - -231 <= nums[i] <= 231 - 1 (small number range)
------
Brute force won't work; there are possibly 20,000 numbers - up to 1 + 2 + 3 + 4 + 5 ... + 20,000 possible subarrays, can't test them all.

What cases exist?
    - All positive, pick entire array
        - [1,2,3]
    - All negative, pick singleton with greatest
        - [-1,-2,-3] -> -1
    - Mix where we can pick a positive-valued contiguous subarray
        - [10,9,-1,8] -> entire array
        - [10,9,-1,8,-2] -> all but last

Tried a few approaches here, specifically one where we find the cumulative sum from right to left, then
left to right; had unfeasible edge cases. This problem can be solved with Kadane's algorithm 
(had to look this up / look at solution; doing this now a bit after and don't remember it fully). 
Going from left to right, we choose the better of the two between starting our subarray at
the particular index, or including it in a running sum:
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        csum = best = -float('inf')
        for val in nums:
            csum = max(val, csum+val)
            best = max(best, csum)
        return best


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
