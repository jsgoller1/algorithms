"""
If we can mutate the grid:
    - do one pass over, launching bfs at each 1 and setting each island to unique id while keeping 
      track of each island's size
    - do another pass over the grid; check each 0 and determine how many islands would be formed by setting it to 1;
      keep track of best this way. 

- Probably very hard to do this in one pass, though if that was important we could do it by checking 0s at the same time as 
  1s, and launch bfs whenever we have neighbors of a 0 who are 1 (land but unvisited)
- can use additional memory if we cannot mutate the grid
"""

from collections import deque
from typing import List


class Solution:
    def get_valid_neighors(self, grid, y, x):
        neighbors = []
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                neighbors.append((ny, nx))
        return neighbors

    def bfs(self, grid, y, x, island_id):
        q = deque([(y, x)])
        grid[y][x] = island_id
        size = 1
        while q:
            y, x = q.popleft()
            for ny, nx in self.get_valid_neighors(grid, y, x):
                if grid[ny][nx] == 1:
                    size += 1
                    grid[ny][nx] = island_id
                    q.append((ny, nx))
        return size

    def get_join_size(self, grid, y, x, island_sizes):
        size = 1
        neighbor_ids = set()
        for ny, nx in self.get_valid_neighors(grid, y, x):
            neighbor_id = grid[ny][nx]
            if neighbor_id not in neighbor_ids:
                neighbor_ids.add(neighbor_id)
                size += island_sizes[neighbor_id]
        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        island_id = 2
        island_sizes = {0: 0}
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 1:
                    island_id += 1
                    island_sizes[island_id] = self.bfs(grid, y, x, island_id)

        largest = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 0:
                    largest = max(largest, self.get_join_size(grid, y, x, island_sizes))
                else:
                    largest = max(largest, island_sizes[cell])
        return largest


s = Solution()
for case in [
    ([[1, 0], [0, 1]], 3),
    ([[1, 1], [1, 0]], 4),
    ([[1, 1], [1, 1]], 4),
    ([[0, 0], [0, 0]], 1),
]:
    grid, expected = case
    actual = s.largestIsland(grid)
    try:
        assert actual == expected
    except AssertionError:
        for row in grid:
            print(" ".join([str(cell) for cell in row]))
        print(f"{actual} != {expected}")
        raise
