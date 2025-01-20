from collections import deque


class Solution:
    def findBuildings(self, heights):
        visible = deque([])
        maxHeight = 0
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > maxHeight:
                visible.appendleft(i)
                maxHeight = heights[i]
        return list(visible)


s = Solution()
for heights, expected in [
    ([4, 2, 3, 1], [0, 2, 3]),
    ([1, 1, 1, 1], [3]),
    ([4, 3, 2, 1], [0, 1, 2, 3]),
    ([1, 3, 2, 4], [3])
]:
    actual = s.findBuildings(heights)
    assert actual == expected, f"{heights}: {actual} != {expected}"
