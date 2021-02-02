from typing import List


def binary_search(row, val):
    lo, hi = 0, len(row)-1
    while lo <= hi:
        mid = (hi+lo) // 2
        if row[mid] == val:
            return mid, True
        elif row[mid] < val:
            lo = mid + 1
        else:
            hi = mid - 1
    return lo, False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], val: int) -> bool:
        # List construction here is O(n) and O(m), but we only do each
        # once regardless of input size.
        lowest_row, found = binary_search([row[-1] for row in matrix], val)
        if found:
            return found
        highest_row, found = binary_search([row[0] for row in matrix], val)
        if found:
            return found

        # if lowest row == 0 and highest row == len(matrix)-1, this becomes
        # O(nlog(m)) for n rows and m columns.
        for y in range(lowest_row, highest_row):
            _, found = binary_search(matrix[y], val)
            if found:
                return found

        return False


cases = [
    ([[1]], 1, True),
    ([[6]], 1, False),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 666, False),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5, True),
]
s = Solution()
for matrix, val, expected in cases:
    actual = s.searchMatrix(matrix, val)
    assert actual == expected, f"{matrix,val}: {expected} != {actual}"
