from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        csum = l = 0
        best = float('inf')
        for r, val in enumerate(nums):
            csum += val
            while csum - nums[l] >= s and l < len(nums):
                csum -= nums[l]
                l += 1
            best = min(r-l+1, best) if csum >= s else best
        return best if best != float('inf') else 0


cases = [
    (7, [2, 3, 1, 2, 4, 3], 2),
    (7, [0, 0, 0], 0),
    (7, [10, 10, 10], 1),
    (7, [], 0)
]

sol = Solution()
for s, nums, expected in cases:
    actual = sol.minSubArrayLen(s, nums)
    assert actual == expected, f"{nums, s}: {expected} != {actual}"
