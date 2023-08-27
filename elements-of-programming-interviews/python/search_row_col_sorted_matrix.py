from typing import List

from test_framework import generic_test


def matrix_search(A: List[List[int]], tgt: int) -> bool:
    y = 0
    x = len(A[0])-1

    while y < len(A) and x >= 0:
        curr = A[y][x]
        if curr == tgt:
            return True
        elif curr > tgt:
            x -= 1
        else:  # curr < tgt
            y += 1

    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_row_col_sorted_matrix.py',
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
