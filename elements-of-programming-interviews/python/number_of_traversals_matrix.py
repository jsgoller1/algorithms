from test_framework import generic_test

"""
- The number of ways to reach any cell is the sum of ways to reach its neighbors
- We don't want to re-visit a cell - for instance if we try to figure out how 
  to visit A, and A's left neigbor is B so we recurse to B, and B's right neighbor is A. 
- What about cycles? Are we only allowing visiting each cell once?

- For a 1xN or Nx1 array, there's 1 way.
- For a 2x2 array, there are 2 ways.
- For a 2x3 / 3x2 array, there are 3 ways. 


recursive pesudo (blows up recursive depth):
    return early if the grid is Nx1 or 1xN (one path) or empty (no paths)
    init a cache (we will map (y,x) -> number of unique acyclic paths to (y,x))
    set cache[(0,1)] and cache[(1,0)] to 1

    def valid(cell):
        return true if cell's y and x are between 0 and rows-1 or cols-1 respectively

    def recursive(current cell, parent cell):
        if current cell is not a key in cache:
            paths = sum the values of recursive(neighbor, current cell) for every valid(neighbor) other than the parent
            cache[cell] = paths
        return cache[cell]
    
    recurse(bottom right, none)
    return cache[bottom right]

iterative pseudo:
    return early if the grid is Nx1 or 1xN (one path) or empty (no paths)
    init a cache (we will map (y,x) -> number of unique acyclic paths to (y,x))
    set cache[(0,1)] and cache[(1,0)] to 1
    init 
       
"""


def number_of_ways(n: int, m: int) -> int:
    if 0 in [n, m]:
        return 0
    if 1 in [n, m]:
        return 1

    cache = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        cache[y][0] = 1
    for x in range(m):
        cache[0][x] = 1

    for y in range(1, n):
        for x in range(1, m):
            cache[y][x] += cache[y-1][x] if 0 <= y else 0
            cache[y][x] += cache[y][x-1] if 0 <= x else 0
    return cache[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_traversals_matrix.py',
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
