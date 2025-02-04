"""
Rotting spreads as BFS. If we queue all the rotting oranges first, then we can 
just BFS as normal. BFS queue contains (orange, rotten_minute) - first ones 
get minute 0. Can either mutate grid or store which oranges are rotten separately;
mutation easier for final scan.

Then once queue is empty, run through the grid and check if any non-rotting
oranges remain. 
"""

from collections import deque


class Solution:
    def anyFresh(self, grid):
        for row in grid:
            for cell in row:
                if cell == 1:
                    return True
        return False

    def getValidNeighbors(self, y, x, grid):
        neighbors = []
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= y + dy < len(grid) and 0 <= x + dx < len(grid[0]):
                neighbors.append((y + dy, x + dx))
        return neighbors

    def orangesRotting(self, grid: List[List[int]]) -> int:
        longest_wait = curr_wait = 0
        q = deque()
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == 2:
                    q.append((y, x, curr_wait))
        while q:
            cy, cx, curr_wait = q.popleft()
            longest_wait = max(curr_wait, longest_wait)
            for ny, nx in self.getValidNeighbors(cy, cx, grid):
                if grid[ny][nx] == 1:
                    grid[ny][nx] = 2
                    q.append((ny, nx, curr_wait + 1))

        return -1 if self.anyFresh(grid) else longest_wait
