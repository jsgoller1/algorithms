from typing import List


class GridUnionFind:
    def __init__(self, m, n):
        self.parent = {}

    def find(self, cell):
        if cell not in self.parent:
            self.parent[cell] = cell

        if self.parent[cell] == cell:
            return cell
        self.parent[cell] = self.find(self.parent[cell])
        return self.parent[cell]

    def union(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.parent[rootA] = rootB


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        land_cells = set()

        def get_land_neighbors(cell):
            y, x = cell
            potential_neighbors = {(y-1, x), (y+1, x), (y, x-1), (y, x+1)}
            return land_cells & potential_neighbors

        positions = [tuple(position) for position in positions]
        uf = GridUnionFind(m, n)
        updates = []
        island_count = 0
        for position in positions:
            if position not in land_cells:
                land_cells.add(position)
                neighbors = get_land_neighbors(position)

                if not neighbors:
                    island_count += 1
                else:
                    island_count -= len(set([uf.find(neighbor) for neighbor in neighbors]))-1

                for neighbor in neighbors:
                    uf.union(neighbor, position)
            updates.append(island_count)
        return updates


s = Solution()
cases = [
    (3, 3, [[0, 0], [0, 1], [1, 2], [1, 2]], [1, 1, 2, 2]),
    (3, 3, [[0, 1], [1, 2], [2, 1], [1, 0], [0, 2], [0, 0], [1, 1]], [1, 2, 3, 4, 3, 2, 1]),
    (2, 2, [[0, 0], [1, 1], [0, 1]], [1, 2, 1])
]
for i, case in enumerate(cases):
    m, n, positions, expected = case
    actual = s.numIslands2(m, n, positions)
    assert actual == expected, f"{i}: {actual} != {expected}"
