"""
- 40 x 40 = 1600 cells total
- k always less than total number of cells
- Start and end are always open 
- return shortest path length, not path itself (suggests DP)

- minimum number of steps to walk suggest BFS
    - Too many cells to try removing as we go?
    - could we BFS and keep track of how many removals we had to perform?
    - Utilize djikstra's with weight/cost/distance including number of eliminated blocks?
        - we want the shortest possible path, not the one with the fewest removals. 

- DP? do we want to find the shortest path to each cell given k allowed removals? 
    - can't use greedy approach: could have edge case where we use too many removals
      to get to intermediary cell when we didn't need to, then can't reach end cell
      (overlapping subproblems)

- problem is also a connected components problem
    - We could build a set of connected components via UF with dfs/bfs from each
      open cell. 
    - This turns into a larger graph where components of open cells are connected 
      via blocked off cells. 


Per discussion with claude:
- BFS will work for this, we just need to maintain multiple states for each cell
- At each cell, we reach it with a certain number of steps and "hammers used" (i.e.
  blocks broken)
- We don't need to try a particular combination of steps and hammers used if it's
  strictly inferior (i.e. shorter path with fewer hammers exists) or partly inferior
  (same len, fewer hammers or same hammers, shorter len)
"""

from typing import List
from collections import defaultdict, deque


class ParetoCache:
    def __init__(self):
        self.data = defaultdict(list)

    def get_shortest_path_len_to_cell(self, y, x):
        return min(self.data[(y, x)])[0] if (y, x) in self.data else -1

    def add_if_dominates(self, y, x, path_len, hammers_used) -> bool:
        """
        The route to (y, x) taking path_len cells via hammers_used
        is on the Pareto curve UNLESS:
        - we have a path of the same length using fewer hammers
        - we have a path using the same number of hammers but shorter length
        - we have a path using fewer hammers and shorter length

        We can probably do this more efficiently with dicts, but here's a quick-and-dirty
        method with a list.

        Returns bool based on whether the path_len, hammers_used was added
        to the list of apporaches.
        """
        # Never seen this cell before
        if (y, x) not in self.data:
            self.data[(y, x)] = [(path_len, hammers_used)]
            return True

        # Seen this cell; check if the approach is optimal
        approaches = self.data[(y, x)]
        i = 0
        while i < len(approaches):
            len_a, hammers_a = approaches[i]

            # An approach with shorter path and fewer hammers
            # exists; proposed path is dominated.
            if len_a <= path_len and hammers_a <= hammers_used:
                return False

            # An approach with same length exists; this one dominates
            # iff it uses fewer hammers.
            elif len_a == path_len:
                dominates = hammers_used < hammers_a
                approaches[i] = (path_len, (min(hammers_a, hammers_used)))
                return dominates

            # Opposite case: an approach using the same number of hammers exists;
            # this one dominates iff it has a shorter path.
            elif hammers_a == hammers_used:
                dominates = path_len < path_a
                approaches[i] = (min(path_len, path_a), hammers_used)
                return dominates

            i += 1

        # We didn't find any approaches that dominate this approach or
        # vice versa; this one now counts as optimal, so add it. It
        # dominates by default
        self.data[(y, x)].append((path_len, hammers_used))
        return True


def get_valid_neighbors(grid, y, x):
    neighbors = []
    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ny, nx = y + dy, x + dx 
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]): 
            neighbors.append((ny, nx))
    return neighbors


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        cache = ParetoCache()
        cache.add_if_dominates(0, 0, 0, 0)
        q = deque([(0, 0, 0, 0)])
        while q:
            y, x, path_len, hammers_used = q.popleft()
            for ny, nx in get_valid_neighbors(grid, y, x):
                n_len, n_hammers = path_len + 1, (hammers_used if grid[ny][nx] == 0 else hammers_used + 1)
                if n_hammers > k: 
                    continue 
                if cache.add_if_dominates(ny, nx, n_len, n_hammers):
                    q.append((ny, nx, n_len, n_hammers))

        return cache.get_shortest_path_len_to_cell(len(grid)-1, len(grid[0])-1)

s = Solution()
for grid, k, expected in [
    ([[0,1,0,0,0,1,0,0],
      [0,1,0,1,0,1,0,1],
      [0,0,0,1,0,0,1,0]], 1, 13),
    ([[0,0,0],
      [1,1,0],
      [0,0,0],
      [0,1,1],
      [0,0,0]], 1, 6),
    ([[0,1,1],
      [1,1,1],
      [1,0,0]], 1, -1),
    ([[0]], 1, 0)
]:
    actual = s.shortestPath(grid, k)
    try:
        assert actual == expected
    except AssertionError:
        for row in grid:
            print(row)
        print(f"{actual} != {expected}")
        raise
