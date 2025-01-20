from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums, k) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)


s = Solution()
for nums, k, expected in [
    ([1, 2, 3, 4], 1, 4),
    ([1, 2, 3, 4], 4, 1),
    ([1, 1, 1, 4], 4, 1),
    ([1, 1, 1, 1], 4, 1),
    ([1, 1, 1, 1], 1, 1),
]:
    actual = s.findKthLargest(nums, k)
    assert actual == expected, f"{k}, {nums}: {actual} != {expected}"
