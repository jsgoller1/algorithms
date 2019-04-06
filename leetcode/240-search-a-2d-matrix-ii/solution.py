"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

- Integers in each row are sorted in ascending from left to right.
- Integers in each column are sorted in ascending from top to bottom.

Example:
Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.
Given target = 20, return false.
------------------------------------
- In: list[int]
- out: bool

- Brute force: linear search entire matrix, O(m*n)
- Slightly better: binary search each row, O(m*log(n))
- We don't need to check a row if its first entry is greater or last
entry is less than the val; if val falls in that range, we do need to check
it though.
- Row entries may overlap; we cannot exclude entire rows unless above condition is met.
- However, by the inpu constraints we should never have a case like:
[9,  21]
[10, 20]
-------------------------------------
For the time being, going to go with m*log(n) strategy;
check array bounds to see if target could fall between them,
skip if not, binary search if so.
"""


class Solution(object):
    def binarySearch(self, row, target):
        l = 0
        r = len(row) - 1
        while l < r - 1:
            mid = (l+r) // 2
            if row[mid] >= target:
                r = mid
            else:
                l = mid
        if target in [row[l], row[r]]:
            return True
        return False

    def searchMatrix(self, matrix, target):
        for y, row in enumerate(matrix):
            if row and row[0] <= target <= row[-1]:
                if self.binarySearch(row, target):
                    return True
        return False


s = Solution()
matrix = [
    [1,   4,  7, 11, 15],
    [2,   5,  8, 12, 19],
    [3,   6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
badMatrix = [[]]

assert s.searchMatrix(matrix, 30) == True
assert s.searchMatrix(matrix, 20) == False
assert s.searchMatrix(badMatrix, 22) == False
