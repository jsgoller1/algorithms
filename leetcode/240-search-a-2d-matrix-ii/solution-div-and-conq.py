from typing import List


def search_matrix(matrix, target, min_y, min_x, max_y, max_x):
    if (min_y, min_x) == (max_y, max_x):
        return matrix[min_y][min_x] == target

    if not matrix[min_y][min_x] <= target <= matrix[max_y][max_x]:
        return False

    mid_row = (max_y + min_y) // 2
    next_row = min(mid_row+1, len(matrix)-1)
    mid_col = (max_x + min_x) // 2
    next_col = min(mid_col+1, len(matrix[0])-1)

    top_left = search_matrix(matrix, target, min_y, min_x, mid_row, mid_col)
    top_right = search_matrix(matrix, target, min_y,  next_col, mid_row, max_x)
    bot_left = search_matrix(matrix, target, next_row, min_x, max_y, mid_col)
    bot_right = search_matrix(matrix, target, next_row, next_col, max_y, max_x)

    return top_left or top_right or bot_left or bot_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], val: int) -> bool:
        return search_matrix(matrix, val, 0, 0, len(matrix)-1, len(matrix[0])-1)


cases = [
    ([[1]], 1, True),
    ([
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ], 20, False)
]
s = Solution()
for matrix, val, expected in cases:
    actual = s.searchMatrix(matrix, val)
    assert actual == expected, f"{matrix,val}: {expected} != {actual}"
