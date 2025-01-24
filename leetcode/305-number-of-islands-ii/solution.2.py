from collections import deque
from typing import List


class UnionFindNode:
    def __init__(self, val):
        self.val = val
        self.parent = self

    def find(self):
        if self.parent == self:
            return self
        self.parent = self.parent.find()
        return self.parent

    def union(self, node2):
        root1 = self.find()
        root2 = node2.find()
        root2.parent = root1


def get_valid_neighbors(grid, y, x):
    neighbors = []
    for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            neighbors.append((ny, nx))
    return neighbors


def get_distinct_neighbor_parents(grid, y, x):
    neighbor_parents = []
    for ny, nx in get_valid_neighbors(grid, y, x):
        if grid[ny][nx].val == 1:
            neighbor_parent = grid[ny][nx].find()
            if neighbor_parent not in neighbor_parents:
                neighbor_parents.append(neighbor_parent)
    return neighbor_parents


def update_islands_n(islands_n, distinct_neighbors_n):
    deltas = {0: 1, 1: 0, 2: -1, 3: -2, 4: -3}
    delta = deltas[distinct_neighbors_n]
    return max(islands_n + delta, 1) if delta < 1 else islands_n + delta


def join_neighbor_parents(node, neighbor_parents):
    for neighbor_parent in neighbor_parents:
        node.union(neighbor_parent)


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        grid = []
        for row in range(m):
            row = []
            for col in range(n):
                row.append(UnionFindNode(0))
            grid.append(row)

        island_counts = []
        islands_n = 0
        for y, x in positions:
            node = grid[y][x]
            if node.val == 0:
                neighbor_parents = get_distinct_neighbor_parents(grid, y, x)
                islands_n = update_islands_n(islands_n, len(neighbor_parents))
                node.val = 1
                join_neighbor_parents(node, neighbor_parents)
            island_counts.append(islands_n)
        return island_counts


s = Solution()
for case in [
    (3, 3, [[0, 0], [0, 1], [1, 2], [2, 1]], [1, 1, 2, 3]),
    (3, 3, [[0, 0], [0, 1], [1, 2], [2, 1], [0, 2]], [1, 1, 2, 3, 2]),
]:
    m, n, positions, expected = case
    actual = s.numIslands2(m, n, positions)
    assert actual == expected, f"{m}, {n}, {positions}: {actual} != {expected}"
