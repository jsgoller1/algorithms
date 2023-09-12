import collections
from typing import List
from collections import deque

WATER = 0
UNVISITED_ISLAND = 1


def valid(grid_height, grid_width, y, x):
    return (0 <= y < grid_height) and (0 <= x < grid_width)


def get_neighbors(grid_height, grid_width, y, x):
    neighbors = [
        (y+1, x),
        (y-1, x),
        (y, x+1),
        (y, x-1),
    ]
    return [neighbor for neighbor in neighbors if valid(grid_height, grid_width, neighbor[0], neighbor[1])]


def identify_component(visited, grid, grid_height, grid_width, y, x, component_id):
    q = deque([(y, x)])
    size = 0
    while q:
        y_c, x_c = q.popleft()
        if (y_c, x_c) in visited:
            continue
        visited.add((y_c, x_c))
        # Must recheck here in case we already changed it
        if grid[y_c][x_c] == UNVISITED_ISLAND:
            grid[y_c][x_c] = component_id
            size += 1
        for y_n, x_n in get_neighbors(grid_height, grid_width, y_c, x_c):
            if grid[y_n][x_n] == UNVISITED_ISLAND:
                q.append((y_n, x_n))
    return size


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        grid_height = len(grid)
        grid_width = len(grid[0])
        visited = set()

        if 0 in [grid_height, grid_width]:
            return 0
        largest_join = 0
        component_id = 2
        component_sizes = {}
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if (y, x) in visited:
                    continue
                if cell == WATER:
                    join = 1
                    joined_components = set()
                    for y_n, x_n in get_neighbors(grid_height, grid_width, y, x):
                        if grid[y_n][x_n] == WATER:
                            continue
                        if grid[y_n][x_n] == UNVISITED_ISLAND:
                            component_id += 1
                            component_sizes[component_id] = identify_component(visited,
                                                                               grid, grid_height, grid_width, y_n, x_n, component_id)
                        neighbor_id = grid[y_n][x_n]
                        join += component_sizes[neighbor_id] if (neighbor_id not in joined_components) else 0
                        joined_components.add(neighbor_id)
                    largest_join = max(largest_join, join)
                    visited.add((y, x))
        return largest_join if largest_join != 0 else len(grid) * len(grid[0])


if __name__ == '__main__':
    cases = [
        ([[]], 0),
        ([[0]], 1),
        ([[1]], 1),
        ([[1, 0]], 2),
        ([[1], [0]], 2),
        ([
            [1, 1, 1],
            [1, 1, 1]
        ], 6),
        ([
            [1, 1, 1],
            [0, 0, 0],
            [1, 1, 1]
        ], 7),
        ([
            [1, 1, 1],
            [0, 1, 0],
            [1, 1, 1]
        ], 8),
        ([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ], 4),
        ([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ], 5),
        ([
            [0],
            [1],
            [0],
            [1]
        ], 3),
        ([
            [0, 1, 0, 1],
        ], 3),
    ]
    for grid, expected in cases:
        s = Solution()
        actual = s.largestIsland(grid)
        try:
            assert actual == expected
        except AssertionError:
            for row in grid:
                print(row)
            print(f"{actual} != {expected}")
            raise

    from massive_test import massive_grid
    import cProfile
    # print(len(massive_grid), len(massive_grid[0]))
    cProfile.run('s.largestIsland(massive_grid)')
    # print(sorted(VISITS.values())[::-1])
