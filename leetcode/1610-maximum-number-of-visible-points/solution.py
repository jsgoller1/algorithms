"""
This problem can be thought of as a sliding window problem. Think about this:

- We can imagine a circle with `location` as the center. Due east is 0 radians/degrees. 
- if `location` is (x,y) and each point is (px, py), then math.atan2(y-py, x-px) measures the angle between 0 deg/rad 
  and (px, py) on the circle centered at `location`, which is effectively `(px, py)`'s position on the circle. 
- If we do that calculation for every point then sort, we have the order of every point along the circle
- `angle` is the size of our window - 0 to angle in size
- then what we maintain is two pointers, l and r, in the sorted array. we move r along until the distance from r to l exceeds angle, at which point we begin to move l up. 
- We need to make sure that we do a full rotation over the circle; the left edge of our viewing window ends at its starting position. We can simulate this by just duplicating
  our sorted list of points, appending it to itself, and then doing our sliding window with the halting position being that arr[l] == arr[0] (and l != 0). 
    - We can also do the above by instead adding every point to the list twice: once, and again with 360 added to its degree value, representing one full rotation
- We need special handling for multiple points at the same location on the circle, as well as points at `location`, which count as always visible. 
"""
from math import atan2, degrees
from collections import Counter, namedtuple

Point = namedtuple('Point', ['degrees', 'count'])

class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        positions = Counter()
        x,y = location
        always_visible = 0
        for px, py in points:
            if x == px and y == py:
                always_visible += 1
                continue
            position = degrees(atan2(py-y, px-x))
            positions[position] += 1
            positions[position + 360.0] += 1
        locations = [Point(loc, count) for loc, count in positions.items()]
        locations.sort()

        count = best = always_visible
        l = r = 0
        while (r < len(locations) and locations[l].degrees-360.0 != locations[0].degrees):
            while locations[r].degrees - locations[l].degrees > angle:
                count -= locations[l].count
                l += 1
            count += locations[r].count
            best = max(best, count)
            r += 1

        return best 


s = Solution()
for points, angle, location, expected in [
    ([[1,1],[2,2],[3,3],[4,4],[1,2],[2,1]], 0, [1,1], 4),
    ([[2,1],[2,2],[3,4],[1,1]], 90, [1,1], 4),
    ([[2,1],[2,2],[3,3]], 90, [1,1], 3),
    ([[1,0],[2,1]], 13, [1,1], 1)
]:
    actual = s.visiblePoints(points, angle, location)
    assert actual == expected, f"{points}, {angle}, {location}: {actual} != {expected}"
