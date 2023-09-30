from typing import List


UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)


class Solution:
    def get_indices(self, mat: List[List[int]]) -> (int, int):
        direction = UP_RIGHT
        y = x = 0
        m, n = len(mat)-1, len(mat[0])-1
        while (y, x) != (m, n):
            yield (y, x)
            if direction == UP_RIGHT:
                if 0 < y and x < n:
                    y, x = y + direction[0], x + direction[1]
                elif x < n:
                    x += 1
                    direction = DOWN_LEFT
                else:
                    y += 1
                    direction = DOWN_LEFT
            else:
                if y < m and 0 < x:
                    y, x = y + direction[0], x + direction[1]
                elif y < m:
                    y += 1
                    direction = UP_RIGHT
                else:
                    x += 1
                    direction = UP_RIGHT
        yield (m, n)

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not (mat and mat[0]):
            return []
        return [mat[y][x] for y, x in self.get_indices(mat)]


s = Solution()
cases = [
    ([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]],
     [1, 2, 4, 7, 5, 3, 6, 8, 9]),
    ([[1, 2],
      [4, 5],
      [7, 8]],
     [1, 2, 4, 7, 5, 8]),
    ([[1, 2, 3],
     [4, 5, 6]],
     [1, 2, 4, 5, 3, 6]),
    ([[1, 2],
     [3, 4]],
     [1, 2, 3, 4])
]
for i, case in enumerate(cases):
    matrix, expected = case
    actual = s.findDiagonalOrder(matrix)
    assert actual == expected, f"{i}: {actual} != {expected}"
