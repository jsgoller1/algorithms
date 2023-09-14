from heapq import heappush, heappop
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        heap = []
        for val, freq in frequencies.items():
            heappush(heap, (freq, val))
            if len(heap) > k:
                heappop(heap)
        return [pair[1] for pair in heap]
