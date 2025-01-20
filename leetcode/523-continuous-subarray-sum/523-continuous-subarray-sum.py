"""
True if (a + b + c ... + d) / k is integer (mod k = 0)
Could this be subarray sum if we preprocess by replacing each val with val % k?
    No
Could we do prefix sums and keep track of remainders? 
    current reminder - some other prefix remainder = 0 and the total array has 2 or more elements, it works
"""
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        prefixes = {}
        rsum = 0
        for i, val in enumerate(nums):
            rsum += val
            remainder = rsum % k
            if (not rsum % k and i > 0) or (remainder in prefixes and prefixes[remainder] < i-1):
                return True
            prefixes[remainder] = i if remainder not in prefixes else prefixes[remainder]
        return False


s = Solution()
for nums, k, expected in [
    ([0, 0, 0], 5, True),
    ([0, 1, 0, 3, 0, 4, 0, 4, 0], 5, False),
    ([1], 1, False),
    ([23, 2, 4, 6, 7], 6, True),
    ([23, 2, 6, 4, 7], 13, False),
    ([100, 200], 10, True)
]:
    actual = s.checkSubarraySum(nums, k)
    assert actual == expected, f"{nums}, {k}: {actual} != {expected}"
