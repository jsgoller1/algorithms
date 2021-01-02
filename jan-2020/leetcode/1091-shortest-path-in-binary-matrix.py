"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is composed of cells C_1, C_2, ..., C_k such that:

    - Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    - C_1 is at location (0, 0) (ie. has value grid[0][0])
    - C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    - If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).

Return the length of the shortest such clear path from top-left to bottom-right.  If such a path does not exist, return -1.

Constraints:
    - 1 <= grid.length == grid[0].length <= 100 (grid will be at most 100 x 100)
    - grid[r][c] is 0 or 1

Possible cases:
    - 1x1 grid
    - 100 x 100 grid
    - all cells blocked
    - no cells blocked
    - terminal cell blocked

Notes:
    - Returning the path length, not the path itself.
    - Diagonal moves are allowed
------------------------------------------------------------------------------
- Shortest path can be solved with BFS, typically.
- We should keep track of visited cells; sometimes you don't need to do this depending on which cells you queue, but there's an edge case here where that breaks.
    - Either need to modify the input graph (more memory efficient) or use separate store (function is pure)
        - Let's modify input; we can use copy.deepcopy() to keep function pure.

bfs:
    queue = deque((root,0))
    while queue:
        current, path_len = queue.popleft()
        if current == target:
            return path_len
        children = get_all_valid_children(current, grid)
        for child in children:
            queue.append((child, path_len+1))
        grid[current[0]][current[1]] = 1
    return -1

get_all_valid_children(cell, grid)
    children = []
    possible_directions = [ ... ]
    for direction in possible_directions:
        y, x = cell[0] + direction[0], cell[1] + direction[1]
        if (0 <= y < len(grid)) and (0 <= x < len(grid[0])) and (grid[y][x] == 0):
            children.append((y,x))
    return children

- Should put check in first to rule out blocked target cell
    - Rules out case of singleton and blocked cell (breaks above)
    - Eliminates wasteful work (but we don't care about this yet)
---------------------
Solved initially with just a BFS; the implementation below uses a priority queue to implement Djikstra's algorithm. Initially, I tried modifying it for 
A* search; it requires using chessboard / Chebyschev distance since diagonals are the same distance as cardinals. Because of some edge cases with finding shorter paths (and
the fact that explaining how this works in an interview is easier than actually implementing it due to details) and the fact that it isn't necessarily a good idea during interviews,
Djikstra's is good enough.
"""
from typing import List
from heapq import heappop, heappush


def get_all_valid_children(cell, grid):
    children = []
    possible_directions = [
        (-1, 0),    # U
        (-1, -1),   # UL
        (0, -1),    # L
        (1, -1),    # DL
        (1, 0),     # D
        (1, 1),     # DR
        (0, 1),     # R
        (-1, 1)     # UR
    ]
    for direction in possible_directions:
        y, x = cell[0] + direction[0], cell[1] + direction[1]
        if (0 <= y < len(grid)) and (0 <= x < len(grid[0])) and (grid[y][x] == 0):
            children.append((y, x))
    # print(f"Valid children of {cell}: {children}")
    return children


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visited = set([(0, 0)])
        target = (len(grid)-1, len(grid[0])-1)
        if 1 in [grid[target[0]][target[1]], grid[0][0]]:
            return -1
        pq = [(1, (0, 0))]
        while pq:
            path_len, current = heappop(pq)
            # print(f"current: {current}, path_len: {path_len}")
            if current == target:
                return path_len
            children = get_all_valid_children(current, grid)
            for child in children:
                if child not in visited:
                    heappush(pq, (path_len+1, child))
                    visited.add(child)
        return -1


if __name__ == '__main__':
    from huge_binary_grid import huge_grid

    sol = Solution()
    cases = [
        ([
            [0, 1],
            [1, 0]], 2),  # given 1
        ([
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]], 4),  # given 2
        ([
            [0, 0, 0],
            [1, 1, 1],
            [1, 1, 0]], -1),  # No path
        ([[1, 0, 0],
          [1, 1, 0],
          [1, 1, 0]], -1),  # Entrance blocked
        ([[0, 0, 0],
          [1, 1, 0],
          [1, 1, 1]], -1),  # Exit blocked
        ([[1]], -1),  # Bad singleton
        ([[0]], 1),  # Good singleton
        ([
            [0, 0, 0, 0, 1, 1, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 0, 1, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 0]], 11),
        (huge_grid, 146)

    ]
    for maze, expected in cases:
        actual = sol.shortestPathBinaryMatrix(maze)
        assert expected == actual, f"{expected} != {actual}"
