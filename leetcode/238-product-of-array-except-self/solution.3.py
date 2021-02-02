from collections import deque
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r_prefix = deque([])
        l_prefix = deque([])
        l_prod = r_prod = 1
        for i, val in enumerate(nums):
            r_prod *= val
            r_prefix.append(r_prod)
            l_prod *= nums[len(nums)-1-i]
            l_prefix.appendleft(l_prod)

        solution = []
        for i, _ in enumerate(nums):
            r = r_prefix[i-1] if i > 0 else 1
            l = l_prefix[i+1] if i < len(nums)-1 else 1
            solution.append(r*l)
        return solution


s = Solution()
assert s.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
assert s.productExceptSelf([0, 1, 2, 4]) == [8, 0, 0, 0]
assert s.productExceptSelf([0, 1, 2, 0]) == [0, 0, 0, 0]
assert s.productExceptSelf([1, 2]) == [2, 1]
