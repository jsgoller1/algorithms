"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from typing import List


class Solution:
    def dfs(self, y, x):
        if not (0 <= y < len(self.grid) and 0 <= x < len(self.grid[0]) and self.grid[y][x] == "1"):
            return
        self.grid[y][x] = "#"
        for dy, dx in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            self.dfs(y + dy, x + dx)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        num_islands = 0
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == "1":
                    num_islands += 1
                    self.dfs(y, x)
        return num_islands


s = Solution()
for grid, expected in [
    ([["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]], 1),
    ([["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"]], 3),
    ([["0"]], 0),
    ([["1"]], 1)
]:
    actual = s.numIslands(grid)
    try:
        assert actual == expected
    except AssertionError:
        for row in grid:
            print(row)
        raise AssertionError(f"{actual} != {expected}")
