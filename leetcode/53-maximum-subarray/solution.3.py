"""
cubic: try all subarrays, recomputing
quadratic: try all subarrays, caching from ends (BFS approach); not viable since n is 100,000
linear: prefix sums could work - take entire array sum first, then calculate prefix sums; 

[-2,  1, -3, 4, -1, 2, 1, -5, 4] (original array)
[-2, -1, -4, 0, -1, 1, 2, -3, 1] -> (prefix sums, calculated L to R)
[ 1,  3,  2, 5,  1, 2, 0, -1, 4] <- (suffix sums, calculated R to L)
"""

from typing import List


# Rolling sum approach with O(c) space; for each value, either include it in the
# ongoing maximum subarray or start a new one from that value.
# Keep track of the maximum seen overall and return it
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        best = max(nums)
        for num in nums:
            total = total + num if total + num > num else num
            best = max(best, total)
        return best


s = Solution()
for nums, expected in [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
]:
    actual = s.maxSubArray(nums)
    assert actual == expected, f"{nums}: {actual} != {expected}"
