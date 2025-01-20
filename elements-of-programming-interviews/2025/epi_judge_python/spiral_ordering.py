from typing import List

from test_framework import generic_test

"""
[
    [1,2,3],
    [8,9,4],
    [7,6,5]
]

"""

RDLU = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    if not (square_matrix and square_matrix[0]):
        return []
    ans = []
    moves = [len(square_matrix[0]), len(square_matrix)-1] 
    moves_i = 0 
    direction_i = 0
    cursor = [0, -1]
    while moves[moves_i]:
        dy, dx = RDLU[direction_i]
        for _ in range(moves[moves_i]):
            cursor[0] += dy 
            cursor[1] += dx 
            ans.append(square_matrix[cursor[0]][cursor[1]])
        moves[moves_i] -= 1
        moves_i = (moves_i + 1) % 2
        direction_i = (direction_i + 1) % 4
    return ans 

arr = [
    [1,2,3],
    [8,9,4],
    [7,6,5]
]
arr = [
    [1,2],
    [8,3],
    [7,4],
    [6,5]
]
assert matrix_in_spiral_order(arr) == [1,2,3,4,5,6,7,8], f"{matrix_in_spiral_order(arr)}"


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
