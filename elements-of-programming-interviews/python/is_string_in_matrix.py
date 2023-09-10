from typing import List

from test_framework import generic_test

"""
Recursive approach:
    - scan entire array one at a time looking for pattern[0]
    - if we find a match, start recursive BFS from that cell looking for pattern[1], etc
    - base case is pattern is empty 
    - O(len(grid) * len(pattern)), possibly - could escalate to nearly n^2 if pattern is in entire grid 

- chars that aren't in our pattern don't matter. 
"""


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    if (not grid) or (not grid[0]):
        return False

    def get_neighbors(y, x):
        return [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]

    def valid(y, x):
        return (0 <= y < len(grid)) and (0 <= x < len(grid[0]))

    def recurse(y, x, p_i):
        if p_i == len(pattern)-1 and pattern[p_i] == grid[y][x]:
            return True
        if not (pattern[p_i] == grid[y][x]):
            return False
        for y2, x2 in get_neighbors(y, x):
            if valid(y2, x2) and recurse(y2, x2, p_i+1):
                return True
        return False

    for y, _ in enumerate(grid):
        for x, _ in enumerate(grid[0]):
            if recurse(y, x, 0):
                return True
    return False


if __name__ == '__main__':
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    cases = [
        ([1, 2, 3], True)
    ]

    for pattern, expected in cases:
        actual = is_pattern_contained_in_grid(grid, pattern)
        assert actual == expected, f"{pattern}: {actual} != {expected}"
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
