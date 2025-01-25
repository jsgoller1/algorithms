"""
I feel like I'm missing an edge case with this approach, but for each row in
 the grid, recursively explore its neighbors:
    - base case: all neighbors are smaller; longest increasing path is 1
    - recursive case: get max of going in any 4 directions (with caching to avoid revisiting)
"""

from typing import List


class Solution:
    def get_valid_neighbors(self, matrix, y, x):
        neighbors = []
        deltas = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dy, dx in deltas:
            ny, nx = y + dy, x + dx
            if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]):
                neighbors.append((ny, nx))
        return neighbors

    def dfs(self, matrix, y, x, visited):
        best = 0
        cell_val = matrix[y][x]
        for neighbor in self.get_valid_neighbors(matrix, y, x):
            ny, nx = neighbor
            if cell_val < matrix[ny][nx]:
                if neighbor not in visited:
                    visited[neighbor] = self.dfs(matrix, ny, nx, visited)
                best = max(best, visited[neighbor])
        return best + 1

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        best = 1
        visited = {}
        for y, row in enumerate(matrix):
            for x, _ in enumerate(row):
                if (y, x) not in visited:
                    best = max(best, self.dfs(matrix, y, x, visited))
        return best


s = Solution()
for case in [
    ([[1, 2], [2, 3]], 3),
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
]:
    matrix, expected = case
    actual = s.longestIncreasingPath(matrix)
    try:
        assert actual == expected
    except AssertionError:
        for row in matrix:
            print(" ".join([str(val) for val in row]))
        print(f"{actual} != {expected}")
