"""
See prefix sums notebook for explanation.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {}
        for i, val in enumerate(nums):
            if val in comps and i != comps[val]:
                return [i, comps[val]]
            comps[target - val] = i
