import heapq
import math


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt(point[0]*point[0] + point[1]*point[1])
            entry = (-distance, point)
            heapq.heappush(heap, entry)
            if len(heap) == k+1:
                heapq.heappop(heap)
        return [entry[1] for entry in heap]
