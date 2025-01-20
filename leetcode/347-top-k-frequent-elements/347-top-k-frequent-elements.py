from heapq import heappush, heappop
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = {}
        for num in nums:
            ctr[num] = ctr[num] + 1 if num in ctr else 1

        heap = []
        for num, count in ctr.items():
            heappush(heap, (count, num))
            if len(heap) > k:
                heappop(heap)

        return [pair[1] for pair in heap]


s = Solution()
for nums, k, expected in [
    ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
    ([1], 1, [1]),
    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ([1, 1, 1, 1], 1, [1])
]:
    actual = s.topKFrequent(nums, k)
    assert sorted(actual) == sorted(
        expected), f"{nums}, {k}: {actual} != {expected}"
