from typing import List

from test_framework import generic_test


def check_row(grid, x):
    elements = set([i for i in range(1,10)])
    for y in range(9):
        val = grid[y][x]
        if val == 0:
            continue
        if val not in elements:
            return False
        elements.remove(val)
    return True

def check_col(grid, y):
    elements = set([i for i in range(1,10)])
    for x in range(9):
        val = grid[y][x]
        if val == 0:
            continue
        if val not in elements:
            return False
        elements.remove(val)
    return True

def check_box(grid, cell):
    elements = set([i for i in range(1,10)])
    y, x = cell 
    for dy in range(y, y+3): 
        for dx in range(x, x+3):
            val = grid[dy][dx]
            if val == 0:
                continue
            if val not in elements:
                return False
            elements.remove(val)
    return True       

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(grid: List[List[int]]) -> bool:
    for i in range(9):
        if not (check_row(grid, i) and check_col(grid, i)):
            return False 
    for top_left in [
        (0,0), (0,3), (0,6),
        (3,0), (3,3), (3,6),
        (6,0), (6,3), (6,6),
    ]:
        if not check_box(grid, top_left):
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
