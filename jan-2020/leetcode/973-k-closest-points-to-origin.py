"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0). (Here, 
the distance between two points on a plane is the Euclidean distance.) You may return the 
answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]

Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:

    1 <= K <= points.length <= 10000
    -10000 < points[i][0] < 10000
    -10000 < points[i][1] < 10000
-----------------------------------------------------
I solved this during my first interviewing.io interview, but my solution was suboptimal. The typical/accepted
solution to this problem is to create a min-heap of size K to store the K-closest, and just return those at the end; 
this is O(n log k). During the mock interview, I created a heap growing to size len(points), which turns the algorithm
into O(n log n), which is no better than just calculating the distance of every point, sorting them, and picking the first K). 
Distance is calculated by Euclidian distance.

How do we construct a minheap of max size k in Python? 
    - can we just remove the last element each time we insert if over capacity? (don't think so)
        - No; the max element is not always at the end of the array, and we could end up removing
          an element less than the max. 
    - We need to remove the maximal element each time we insert if over capacity 
    - We could maintain a minheap and a maxheap. Each time we insert, we insert into both. If we go over capacity,
      pop the top of the maxheap, and replace that item in the minheap.
        - How would we efficiently find that the value in the minheap though?
    - Do we actually need to use a minheap? What if we just used a maxheap of the inverse distances?

Also, this problem asks to find k closest to the origin; the one from the interview gave a specific point. 
"""
import heapq
import math
from typing import List


def distance(p1, p2):
    x0, y0 = p1
    x1, y1 = p2
    return math.sqrt((x1-x0)**2+(y1-y0)**2)


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        if k >= len(points):
            return points

        maxheap = []
        for point in points:
            dist = distance(point, (0, 0))
            heapq.heappush(maxheap, (-dist, point))
            if len(maxheap) > K:
                heapq.heappop(maxheap)

        return [point for _, point in maxheap]


s = Solution()
cases = [
    ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]])
]
for points, k, expected in cases:
    actual = s.kClosest(points, k)
    assert sorted(expected) == sorted(actual), f"{points, k}: {sorted(expected)} != {sorted(actual)}"
