"""
Good ol' spiral print

constraints:
    m == matrix.length (rows)
    n == matrix[i].length (cols)
    1 <= m, n <= 10 (at most 10x10 matrix)
    -100 <= matrix[i][j] <= 100
---------------------------------------------
This was my TPS question at ATG!

There's two approaches to this (at least):
    - "Sentinel values" - keep track of what the topmost, leftmost, rightmost, and bottomost indexes should be while printing,
                          and decrement. I've only seen this approach work once; very error prone.
    - Cursor approach, described below

- If we have an m-by-n matrix, and we go in R-D-L-U order, we print as follows:
N R
M-1 D
N-1 L
M-2 U
N-2 R
....
1 U
1 R
Halt
(until we reach 0)

So instead of trying to keep track of sentinel values, we can just store directions, and move that many until we reach zero.

Some odd edge cases:
    - N != M (6x2); make sure to check both cases
    - N = M = 1
----------------------------------------------------------------
approach(matrix):
    solution = []
    moves = [right,down,left,up as coordinates (e.g. (0, 1) for right)]
    next_move = 0
    current_cell = (0,0)
    N = cols count
    M = rows count
    while N and M are both greater than 0: # need to check both
        # get next move
        next move count = N if L/R, M if U/D
        if we didn't decrement this move count last time, do it now

        for each next move:
            add move to current cell
            add current cell to solution
        increment next move
    return solution
"""
from typing import List

#              RIGHT,  DOWN,    LEFT,     UP
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        solution = []
        direction_i = 0
        current_cell = [0, -1]
        moves, next_moves = len(matrix[0]), len(matrix)-1

        while moves:
            next_move = DIRECTIONS[direction_i]

            for _ in range(moves):
                current_cell[0] += next_move[0]
                current_cell[1] += next_move[1]
                solution.append(matrix[current_cell[0]][current_cell[1]])

            direction_i = (direction_i + 1) % 4
            moves, next_moves = next_moves, moves-1

        return solution


if __name__ == '__main__':
    sol = Solution()
    cases = [
        ([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7])
    ]
    for matrix, expected in cases:
        actual = sol.spiralOrder(matrix)
        assert expected == actual, f"{expected} != {actual}"
