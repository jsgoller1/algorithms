from typing import List

"""
- each cell has between 2 and 4 neighbors, so there are at minimum O(2^m*n) possible paths, which for a 25x25 matrix will
  be intractible. 
- Recurrence:
    - base: no neighors are greater than cell. Path starting there is 1.
    - recursive: path is 1 plus largest path of all increasing neighbor.
- the starting point may not be the smallest value in the matrix; we could have only two (disconnected)
    increasing paths 0-1-2 and 4,5,6,7 
- We can make c passes over the array while finding solution in linear time

- increasing paths are just decreasing paths in reverse; we could start from the largest element. 
- Could we just go cell by cell, launching BFS and trying to make a _decreasing_ path? We keep track
  of cells we've already visited and add their lengths to neighbors if applicable; only need to visit each
  cell once, so it's linear time and space. 
  - What edge case does this fail on?
    - BFS will be shortest path but only if we terminate on finding a particular node
    - DFS / recursive will make it a bit easier to implement; can have 200 x 200 node = 4000 len paths.
      this could blow up 3000 default limit. Can implement iteratively keeping track of parent state? 
    - won't work if the starting cell has path length 1; what if a cell next to it should be on the path?

- a recursive approach where we identify the longest path leading up to the current cell will work, because if a neighbor cell
  is smaller we recurse onto it, and if one is larger, it can just look at the length of the current cell when we get to it.
- the size of the grid could lead to a 200 x 200 grid, which will have 4000 cells, so we can't use real recursion but we could
  simulate it iteratively with a stack. 
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) < 2 and len(matrix[0]) < 2:
            return 1

        visited = {}
        longest = 1

        def valid(y: int, x: int) -> bool:
            return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])

        def decreasing(c_y: int, c_x: int, n_y: int, n_x: int):
            return matrix[c_y][c_x] > matrix[n_y][n_x]

        def get_visitable_neighbors(y: int, x: int):
            possible = [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]
            return [(n_y, n_x) for n_y, n_x in possible if valid(n_y, n_x) and decreasing(y, x, n_y, n_x)]

        def dfs(y: int, x: int):
            # NOTE: the constraints on this problem allow for 200 x 200 = 4000 cells.
            # It's very possible this DFS will exceed recursive depth limit.
            best_len = 1
            for n_y, n_x in get_visitable_neighbors(y, x):
                if (n_y, n_x) in visited:
                    best_len = max(best_len, visited[(n_y, n_x)]+1)
                else:
                    best_len = max(best_len, dfs(n_y, n_x)+1)
            visited[(y, x)] = best_len
            return best_len

        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if (y, x) not in visited:
                    longest = max(longest, dfs(y, x))
        print(visited)
        return longest


s = Solution()
cases = [
    (
        [[9,  8, 7],
         [10, 9, 6],
         [11, 5, 4]], 7
    ),
    (
        [[9,  8, 7],
         [7, 9, 6],
         [11, 5, 4]], 5
    ),
    (
        [[1, 1, 1],
         [1, 1, 1],
         [1, 1, 1]], 1
    ),
    (
        [[1]], 1
    ),
    (
        [[3, 4, 5],
         [3, 2, 6],
         [2, 2, 1]], 4
    )
]

for maze, expected in cases:
    print("-------")
    actual = s.longestIncreasingPath(maze)
    try:
        assert actual == expected
    except AssertionError:
        for row in maze:
            print(row)
        print(f"{actual} != {expected}")
        raise
