from typing import List

from test_framework import generic_test


"""
Min weight to given cell is the less of the two paths leading to it. 
Can definitely utilize caching 
"""


def minimum_path_weight(triangle: List[List[int]]) -> int:
    if (not triangle) or (not triangle[0]):
        return 0
    cache = {}

    def recurse(row_no, cell_no) -> int:
        # base case is lowest level of triangle, otherwise pick lesser of two children
        if row_no == len(triangle)-1:
            return triangle[row_no][cell_no]
        if (row_no, cell_no) not in cache:
            left_path = recurse(row_no+1, cell_no)
            right_path = recurse(row_no+1, cell_no+1)
            cache[(row_no, cell_no)] = min(left_path, right_path) + triangle[row_no][cell_no]
        return cache[(row_no, cell_no)]

    return recurse(0, 0)


if __name__ == '__main__':
    cases = [
        ([[]], 0),
        ([
            [1],
            [2, 3]
        ], 3),
        ([
            [1],
            [2, 3],
            [4, 5, 6]
        ], 7),
        ([
            [7],
            [1, 2],
            [4, 5, 2]
        ], 11)
    ]
    for triangle, expected in cases:
        actual = minimum_path_weight(triangle)
        try:
            assert actual == expected
        except AssertionError:
            print(f"{actual} != {expected}")
            for row in triangle:
                print(row)

    exit(
        generic_test.generic_test_main(
            'minimum_weight_path_in_a_triangle.py',
            'minimum_weight_path_in_a_triangle.tsv', minimum_path_weight))
