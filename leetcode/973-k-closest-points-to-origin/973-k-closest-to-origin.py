from math import sqrt
from heapq import heappop, heappush


class Solution:
    def distance(self, point):
        return sqrt(point[0]**2 + point[1]**2)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            heappush(heap, (-self.distance(point), point))
            if len(heap) > k:
                heappop(heap)
        return [entry[1] for entry in heap]
