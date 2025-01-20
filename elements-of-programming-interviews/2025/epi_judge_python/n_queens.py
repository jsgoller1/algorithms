from typing import List

from test_framework import generic_test

"""
Solution is for what row or column the queens go in; we don't need
to specify both since if we put two in the same row/column, it's not a solution. 
- if we didn't care about diagonal, we would just place all in different rows in any order:
[1,2,3,4], [1,3,4,2], etc.
- diagonal means we cannot simultaneously place:
    - (x,x) and (y,y) for any y != x
    - (x,x) and (x+1,x+1)
    - x,y and 

- we can fit n queens on the board for n >= 4. 1 has 1 solution, 2 and 3 have none, and 4 has 2. 
- for n=5, solve n=4. Then for each of the n=4 cases, we have 4 possible solutions for 8 total.
"""

def n_queens(n: int) -> List[List[int]]:
    if n < 4:
        return [] if n in [0,2,3] else [[0]]
    solutions = []
    def recurse(curr_placement, diags, antidiags, rows, col):
        if col == n:
            solutions.append(curr_placement)
            return
        for row in range(n): 
            if not (row in rows or row-col in diags or row+col in antidiags):
                recurse(curr_placement + [row], diags | {row-col}, antidiags | {row+col}, rows | {row}, col+1) 
    recurse([], set(), set(), set(), 0)
    return solutions 


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
