from collections import deque
from typing import List

DIAGONALS = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
COMPASS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIRECTIONS = COMPASS + DIAGONALS


class Solution:
    def getValidNeighbors(self, y, x, grid):
        neighbors = []
        for dy, dx in DIRECTIONS:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]) and grid[new_y][new_x] == 0:
                neighbors.append((new_y, new_x))
        return neighbors

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        queue = deque([(1, 0, 0)])
        visited = set([])
        while queue:
            pathlen, y, x = queue.popleft()
            if (y, x) in visited:
                continue
            visited.add((y, x))
            if (y, x) == (len(grid)-1, len(grid[0])-1):
                return pathlen
            for y, x in self.getValidNeighbors(y, x, grid):
                queue.append((pathlen+1, y, x))
        return -1


s = Solution()
for grid, pathlen in [
    ([[0, 1], [1, 0]], 2),
    ([[0, 0, 0],
      [1, 1, 0],
      [1, 1, 0]], 4),
    ([[1, 0, 0],
      [1, 1, 0],
      [1, 1, 0]], -1)
]:
    actual = s.shortestPathBinaryMatrix(grid)
    try:
        assert actual == pathlen
    except AssertionError:
        for row in grid:
            print(row)
        print(f"{actual} != {pathlen}")
        raise
