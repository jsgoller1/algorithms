# k = rsum - prevseen
# k - rsum = - prevseen
# 10 = 15 - 5 -> 10 - 15 = -5
# -15 = -10 - 5 -> -15 + 10 = -5

from typing import List
from collections import Counter


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixes = Counter({0: 1})
        count = 0
        rsum = 0
        for val in nums:
            rsum += val
            count += prefixes[rsum-k]
            prefixes[rsum] += 1
        return count


s = Solution()
for nums, k, expected in [
    ([1], 1, 1),
    ([1], 3, 0),
    ([1, 1, 1], 1, 3),
    ([1, 1, 1], 2, 2),
    ([1, 1, 1], 3, 1),
    ([1, -1, 1, 0], 0, 4)

]:
    actual = s.subarraySum(nums, k)
    assert actual == expected, f"{nums}, {k}: {actual} != {expected}"
    print("----")
