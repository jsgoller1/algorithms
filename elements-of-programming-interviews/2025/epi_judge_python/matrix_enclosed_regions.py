from typing import List

from test_framework import generic_test

"""
for each non-border W cell, launch BFS (with visited set)
- keep track of other W cells found during said bfs
- if cells are not enclosed do nothing; if they are, paint them
- visits each cell at most twice

could also launch bfs from each W border cell, put some other string in found W cell,
then flip entire board after (still visiting twice though)
"""

from collections import deque

def paint(board, cells):
    for cell in cells:
        y, x = cell 
        board[y][x] = 'B'

def is_open_border_cell(board, y,x):
    entry = board[y][x]
    return (y in [0, len(board)-1] or x in [0, len(board[0])-1]) and entry == 'W'

def get_valid_neighbors(board, y, x):
    out = []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < len(board) and 0 <= nx < len(board[0]):
            out.append((ny, nx))
    return out

def bfs(board, y, x, visited):
    cells = set([])
    reachable = False
    q = deque([(y,x)])
    while q:
        y, x = q.popleft()
        cells.add((y,x))
        reachable |= is_open_border_cell(board, y, x)
        for neighbor in get_valid_neighbors(board, y, x):
            y, x = neighbor
            if neighbor not in visited and board[y][x] == 'W':
                visited.add(neighbor)
                q.append(neighbor)
    return reachable, cells 


def fill_surrounded_regions(board: List[List[str]]) -> None:
    visited = set()
    for y, row in enumerate(board):
        for x, entry in enumerate(row):
            if 0 < y < len(board)-1 and 0 < x < len(board[0])-1 and (y,x) not in visited and entry == 'W':
                reachable, cells = bfs(board, y, x, visited)
                if not reachable:
                    paint(board, cells)
    return


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board

for board, expected in [
    (
        [
            ["B", "W", "B", "B"],
            ["B", "W", "W", "B"],
            ["B", "W", "W", "B"],
            ["B", "B", "B", "B"],
        ],
        [
             ["B", "W", "B", "B"],
            ["B", "W", "W", "B"],
            ["B", "W", "W", "B"],
            ["B", "B", "B", "B"],
        ],    
    )
]:
    #print("Board")
    #for row in board:
    #    print(row)
    #fill_surrounded_regions(board)
    try:
        assert board == expected
    except AssertionError:
        print("\nExpected")
        for row in expected:
            print(row)
        print("\nActual")
        for row in board:
            print(row)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
