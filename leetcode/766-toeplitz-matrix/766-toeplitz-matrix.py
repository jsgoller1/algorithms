def hasValidDiagAncestor(y, x):
    return y-1 >= 0 and x-1 >= 0


def diagMatches(matrix, y, x):
    return matrix[y][x] == matrix[y-1][x-1]


class Solution:
    def isToeplitzMatrix(self, matrix) -> bool:
        for y, row in enumerate(matrix):
            for x, col in enumerate(row):
                if hasValidDiagAncestor(y, x) and not diagMatches(matrix, y, x):
                    return False
        return True


s = Solution()
for matrix, expected in [
    ([[0]], True),
    ([[1, 2], [3, 4]], False),
    ([[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True)
]:
    actual = s.isToeplitzMatrix(matrix)
    assert actual == expected, f"{actual} != {expected} for \n{matrix}"
