from typing import List

from test_framework import generic_test

"""
Several ways we could do this:
- check every cell along the border; launch BFS from all white border cells and add
reachable cells to "do not flip" set. Then go over the entire matrix and flip any white
cell in the "do not flip" set.
- go over every cell in matrix. If a cell is white, check if we can reach the border from it. If not,
flip all cells connected to it. 
- Go over every cell in matrix, keeping track of separate connected components of white cells
(give each a number). Do this by launching a DFS from each white cell, changing its contents to the
number associated with its connected component. If the DFS reaches the border, put the ID in a do-not-flip set.
Then go over the entire matrix once; if a cell's id is in the do-not-flip list, set it to white. Otherwise, set it
to black. 

All can be done in involve O(n) time, and close to O(n) space. 
"""


def is_border(board, y, x):
    return y == 0 or y == len(board)-1 or x == 0 or x == len(board[0])-1


def is_valid(board, y, x):
    return 0 <= y < len(board) and 0 <= x < len(board[0])


def reaches_border(board, y, x, visited):
    stack = [(y, x)]
    reached_border = False
    while stack:
        c_y, c_x = stack.pop()
        if not reached_border:
            reached_border = is_border(board, c_y, c_x)
        visited.add((c_y, c_x))
        for n_y, n_x in [(c_y+1, c_x), (c_y-1, c_x), (c_y, c_x+1), (c_y, c_x-1)]:
            if is_valid(board, n_y, n_x) and (n_y, n_x) not in visited and board[n_y][n_x] == 'W':
                stack.append((n_y, n_x))
    return reached_border


def flood_fill(board, color, y, x):
    stack = [(y, x)]
    while stack:
        c_y, c_x = stack.pop()
        board[c_y][c_x] = color
        for n_y, n_x in [(c_y+1, c_x), (c_y-1, c_x), (c_y, c_x+1), (c_y, c_x-1)]:
            if is_valid(board, n_y, n_x) and board[n_y][n_x] != color:
                stack.append((n_y, n_x))


def fill_surrounded_regions(board: List[List[str]]) -> None:
    if not (board and board[0]):
        return

    visited = set()
    for y, row in enumerate(board):
        for x, color in enumerate(row):
            if color == 'W' and (y, x) not in visited:
                if not reaches_border(board, y, x, visited):
                    flood_fill(board, 'B', y, x)
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    """
    maze = [
        ['B', 'B', 'B', 'B', 'B'],
        ['B', 'W', 'B', 'B', 'B'],
        ['B', 'W', 'W', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B'],
        ['B', 'W', 'B', 'W', 'B'],
        ['B', 'B', 'B', 'W', 'B'],
    ]
    for row in maze:
        print(row)
    fill_surrounded_regions(maze)
    print("---------")
    for row in maze:
        print(row)

    """
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
