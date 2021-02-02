"""
See prefix sums notebook for explanation.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, val in enumerate(nums):
            if val in comps and i != comps[val]:
                return [i, comps[val]]
            comps[target - val] = i


s = Solution()
cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([-1, -2, -3, -4, -5], -8, [2, 4])
]
for arr, target, expected in cases:
    actual = s.twoSum(arr, target)
    assert sorted(expected) == sorted(actual), f"arr,target: {expected} != {actual}"
