from typing import List
from collections import deque

DIRECTIONS = [
    (-1, 0),  # N
    (-1, 1),  # NE
    (0, 1),  # E
    (1, 1),  # SE
    (1, 0),  # S
    (1, -1),  # SW
    (0, -1),  # W
    (-1, -1)  # NW
]


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(y, x):
            return 0 <= y < len(grid) and 0 <= x < len(grid[0])

        n = len(grid)-1
        q = deque([(0, 0, 1)])
        while q:
            y, x, pathlen = q.popleft()
            if y == x == n:
                return pathlen
            for delta_y, delta_x in DIRECTIONS:
                y_n, x_n = y + delta_y, x + delta_x
                if valid(y_n, x_n) and grid[y_n][x_n] == 0:
                    q.append((y_n, x_n, pathlen+1))
                    grid[y_n][x_n] = 1
        return -1


s = Solution()
cases = [
    ([[0]], 1),  # if start == stop, no traversal needed
    ([[1]], -1),  # if start == stop, no traversal needed
    ([
        [0, 1],
        [1, 0]
    ], 2),
    ([
        [0, 0],
        [0, 0],
    ], 2),
    ([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ], 3),
    ([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ], 4),
    ([
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0],
    ], -1),
]
for maze, expected in cases:
    actual = s.shortestPathBinaryMatrix(maze)
    try:
        for row in maze:
            print(row)
        print("----")
        assert expected == actual
    except AssertionError:
        print(f"{actual} != {expected}")
        raise
