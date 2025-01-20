"""
Min cost to paint 0th house: min available 
Cost to paint 1th house: min of (r + prev house not red, b + prev house not b, g + prev house not g)
"""
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        prev_nonred = prev_nonblue = prev_nongreen = 0
        paint_red = paint_blue = paint_green = 0
        for red, blue, green in costs:
            paint_red = red + prev_nonred
            paint_blue = blue + prev_nonblue
            paint_green = green + prev_nongreen

            prev_nonred = min(paint_blue, paint_green)
            prev_nonblue = min(paint_red, paint_green)
            prev_nongreen = min(paint_red, paint_blue)

        return min(prev_nonred, prev_nonblue, prev_nongreen)


s = Solution()
for costs, expected in [
    ([[1, 1, 1], [1, 1, 1], [1, 1, 1]], 3),
    ([[7, 6, 2]], 2),
    ([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10)
]:
    actual = s.minCost(costs)
    assert actual == expected, f"{costs}: {actual} != {expected}"
