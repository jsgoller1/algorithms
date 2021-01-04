"""
Given an array of integers, return a new array such that
each element is the product of all other elements in the original array,
excluding the one at that index.

Followup: what if you cannot use division?
Followup: Can you solve it with constant space?

(Leetcode #238)

Constraints:
    product of entire array will be between 0 and 2**32 -1

--------------------
    - Array could be huge, contain zeros, and will have at least one element

    With division:
        Get product of entire array, then set each element to it but / the element at that index; O(n) space and time.

    Without division, O(n) space:
        Use a left-array (products up to i starting from the left) and right array;
        for each value in output array, combine neighbor left neighbor from left array and right neighbor from right array

    Without division, O(1) space (not counting ouput array):
        In: [1,2,3,4,5]
        with current = 1 = without current:
        Doing left pass:
            with_current = 1, without_current = 1, [1],
            with_current = 2, without_current = 1  [1, 1]
            with_current = 6, without_current = 2  [1, 1, 2]
            with_current = 24, without_current = 6  [1, 1, 2, 6]
            with_current = 121, without_current = 24  [1, 1, 2, 6, 24]
        Doing right pass; multiple with existing entry
            with_current = 5, without_current = 1  [1, 1, 2, 6, 24]
            with_current = 20, without_current = 5  [1, 1, 2, 30, 24]
            with_current = 60, without_current = 20  [1, 1, 40, 30, 24]
            with_current = 120, without_current = 60  [1, 60, 40, 30, 24]
            with_current = 120, without_current = 60  [120, 60, 40, 30, 24]

        Initialize solution array using all 1s
        Start with two values, using_current, no_current set to 1
        From left to right:
            multiply current entry in source by using_current
            multiply current entry in solution by no_current
            set no_current to using current, go to next entry
        Do same procedure from right to left
        Return result
"""
from typing import List


class Solution:
    def _non_self_products(self, indexes):
        use_current = no_current = 1
        for i in indexes:
            use_current *= self.nums[i]
            self.products[i] *= no_current
            no_current = use_current

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.products = [1 for i in nums]
        indexes = [i for i, _ in enumerate(nums)]

        self._non_self_products(indexes)
        indexes.reverse()
        self._non_self_products(indexes)

        return self.products


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([1, 2, 3, 0], [0, 0, 0, 6]),
        ([0, 2, 3, 0], [0, 0, 0, 0]),
        ([1], [1]),
        ([1, 2], [2, 1]),
    ]
    for input_args, expected in cases:
        actual = s.productExceptSelf(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
