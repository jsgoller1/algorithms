"""
Visit every 0 cell once: tree? Can't have cycles.
Hamiltonian path: visits each vertex exactly once; needs to start at 1, end at 0, and not visit -1.
Start at 2? does that help at all?
max cells - 400 (20 x 20); n^2 is 160000, so this is viable

=== Brute force / DFS approach ===
- Count number of -1 beforehand
- Do regular DFS starting at 1, except can't visit -1, can't revisit, and can't visit 2 unless n*m-(count of -1) cells have been visited
- Return 1 if we reach 2, return 0 otherwise
- Can we do this but prune?

=== DP approach ===
- "Hamiltonian Zero Path" (HZP): path in grid starting at start, reaching target cell, crossing every 0 only once.
- Num of HZP(1,2): sum of HZP(1, neighbor) for each of 2's neighbors (each is unique since they end at a different neighbor)
    - This doesn't hold for a 2x2 -> 3x3 grid; adding cells changes whether a previously reachable cell is reachable or not.
- 1x1 is not valid input. 2x1, 1x2 are trivial; 1 path.
- 2x2 has one allowed for only one graph:
    [1, 2]
    [0, 0] (D-R-U)
    - Any other arrangement (not counting rotations) has no solution
    - Any 2x2 with nonzero -1s has no solution

This has 4 ways to make acyclic paths of len 12.
[1, 0, 0, 0]
[0, 0, 0, 0]
[0, 0, 0, 2]

Grid          Recurrence for HZPs (X == -1)
[1, 0, 0, 0]  ->    [1, 0, 0, 0]
[0, 0, 0, 0]        [0, 0, 0, 2]  2 ways for acyclic paths of len 11
[0, 0, 0, 2]        [0, 0, 0, X]
                        +
                    [1, 0, 0, 0]
                    [0, 0, 0, 0]  2 ways for acyclic paths of len 11
                    [0, 0, 2, X]

Does this strategy evaluate paths it doesn't need to? Doesn't seem different
from just trying a quadratic DFS from 1.
- Don't need to repeatedly try to find (y,x,k), i.e. count of valid k-len paths to grid[y,x]
- Do we need to try (y,x,k) and (y,x,n) if n != k? some paths may take (y,x) as the nth node, others as the kth node.

Trying smaller example:
This has 1 way to make acyclic path of len 5.
[1, 0, 0]
[0, 0, 2]


Grid          Recurrence for HZPs (X == -1)
[1, 0, 0]  ->   [1, 0, 2] 1 path
[0, 0, 2]       [0, 0, x]
                  +
                [1, 0, 0]
                [0, 2, X] 0 paths

[1, 2, X]  -> .... (etc)
[0, 0, X]

"""
from typing import List


def is_valid(grid, y, x):
    return (0 <= y < len(grid)) and (0 <= x < len(grid[0]))


def get_neighbors(grid, y, x):
    neighbors = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbors.append((y+dy, x+dx)) if is_valid(grid, y+dy, x+dx) else None
    return neighbors


def dfs(grid, y, x, path_len, visited):
    cell = grid[y][x]
    if (y, x) in visited or cell == -1:
        return 0
    if cell == 2:
        return 1 if path_len == 0 else 0

    paths = 0
    visited.add((y, x))
    for y_n, x_n in get_neighbors(grid, y, x):
        paths += dfs(grid, y_n, x_n, path_len-1, visited)
    visited.remove((y, x))
    return paths


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        start_y = start_x = 0
        required_cells = len(grid) * len(grid[0])
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell == -1:
                    required_cells -= 1
                elif cell == 1:
                    start_y, start_x = y, x
                    required_cells -= 1
        return dfs(grid, start_y, start_x, required_cells, set())


s = Solution()
cases = [
    ([
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 2, -1]], 2),
    ([
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 2]], 4),
    ([
        [0, 1],
        [2, 0]], 0),
]
for grid, expected in cases:
    actual = s.uniquePathsIII(grid)
    try:
        assert actual == expected
    except AssertionError:
        print("=="*10)
        for row in grid:
            print(row)
        print(f"{expected} != {actual}")
        raise
