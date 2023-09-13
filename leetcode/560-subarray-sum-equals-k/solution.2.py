"""
brute_force()
    curr_sum = sum(arr)
    recursive(l, r, k, curr_sum):
        if l > r:
            return 0
        total = 1 if k == curr_sum else 0
        total += recursive(l+1, r, k, curr_sum-arr[l])
        total += recursive(l, r-1, k, curr_sum-arr[r])
        return total
return recursive(0, len(arr)-1, k, curr_sum)

"""
from collections import Counter
from typing import List
import random


class Solution:
    def brute_force_recursive(self, nums: List[int], k: int) -> int:
        cache = {}

        def recursive(l, r, k, curr_sum):
            if l > r:
                return 0
            if (l, r) not in cache:
                total = 1 if k == curr_sum else 0
                total += recursive(l+1, r, k, curr_sum-arr[l])
                total += recursive(l, r-1, k, curr_sum-arr[r])
                cache[(l, r)] = total
                return cache[(l, r)]
            return 0

        curr_sum = sum(arr)
        return recursive(0, len(arr)-1, k, curr_sum)

    def subarraySum(self, nums: List[int], k: int) -> int:
        total = subarrays = 0
        prefixes = Counter({0: 1})
        for val in nums:
            total += val
            subarrays += prefixes[total - k]
            prefixes[total] += 1
        return subarrays


cases = [
    ([], 5, 0),
    ([1], 5, 0),
    ([1], 1, 1),
    ([1], 0, 0),
    ([1, 1, 1], 1, 3),
    ([1, 2, 3], 3, 2),
    ([-1, -1, 1], 0, 1)
    # ([random.randint(-10**7, 10**7) for _ in range(2*10**4)], 25, -1)

]
s = Solution()
for arr, k, expected in cases:
    actual = s.subarraySum(arr, k)
    assert actual == expected, f"{arr}, k = {k}: {actual} (actual) != {expected} (expected)"
