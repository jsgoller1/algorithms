from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarrays = csum = 0
        prefixes = defaultdict(int)
        prefixes[csum+k] += 1
        for val in nums:
            csum += val
            subarrays = subarrays + prefixes[csum]
            prefixes[csum+k] += 1
        return subarrays


s = Solution()
cases = [
    ([1, 1, 1], 2, 2),
    ([1, 2, 3], 3, 2),
    ([4, -1, 1, 2, 3], 3, 3)
]
for arr, val, expected in cases:
    actual = s.subarraySum(arr, val)
    assert expected == actual, f"{arr,val}: {expected} != {actual}"
