from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = ans = 0
        prod = 1
        for r, val in enumerate(nums):
            prod *= val
            while prod >= k and l < len(nums):
                prod /= nums[l]
                l += 1
            ans += r-l+1 if prod < k else 0
        return ans


s = Solution()
cases = [
    ([10, 5, 2, 6], 100, 8),
    ([10, 5, 1, 2, 6], 100, 13),
    ([1, 2, 3], 0, 0)
]
for arr, target, expected in cases:
    actual = s.numSubarrayProductLessThanK(arr, target)
    assert actual == expected, f"{arr,target}; {expected} != {actual}"
