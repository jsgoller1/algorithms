from typing import List

from test_framework import generic_test

"""
This seems like it's just spiral print, but involves swapping elements with itself?
Easier: transpose then rotate on y axis.

"""

def transpose_swap(square_matrix, diag_idx):
    # Swap the 0th row and column of the submatrix whose 0th diagonal equals the ith diagonal of the square matrix. 
    y = x = diag_idx
    delta = 1
    while y + delta < len(square_matrix):
        square_matrix[y + delta][x], square_matrix[y][x + delta] = square_matrix[y][x + delta], square_matrix[y + delta][x]
        delta += 1

def transpose(square_matrix):
    # Do the transpose swap for each diagonal
    for i, _ in enumerate(square_matrix):
        transpose_swap(square_matrix, i)

def rotate(square_matrix):
    for row in square_matrix:
        row.reverse()

def rotate_matrix(square_matrix: List[List[int]]) -> None:
    transpose(square_matrix)
    rotate(square_matrix)
    return


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
