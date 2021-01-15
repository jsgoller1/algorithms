"""
Unlike my other solution this one is O(n*log(k)), which
is slightly more efficient than sorting the entire
array. 
"""

from heapq import heappush, heappop


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for val in nums:
            heappush(heap, val)
            if len(heap) > k:
                heappop(heap)
        return heappop(heap)
