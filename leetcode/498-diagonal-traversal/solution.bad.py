"""
2x3:
UR 1
DL 2
UR 2
DL 1

3x2:
UR 1
DL 2
UR 2
DL 1


3x3:
UR 1
DL 2
UR 3
DL 2
UR 1


(0,0)
(0,1)
(2,0)
(1,2)
(2,2)


"cursor":
    - start at 0,0, end at m-1, n-1
    - move up/right then down/left
    - increase move distance on each alternation til we reach min(m,n) then decrease
    - get next start point:
        - UR always moves 1 right until it can't, then moves 1 down
        - DL moves down until it can't, then moves right
    - if last beginning was m-1, n-1, end. 

"""
from typing import List


UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not (mat and mat[0]):
            return []

        m = len(mat)-1
        n = len(mat[0])-1
        cursor = (0, 0)
        distance = 0
        direction = UP_RIGHT
        solution = []
        decreasing = False
        print(f"{m+1} x {n+1}")
        print(f"cursor: {cursor} (initial)")
        while cursor != (m, n):
            print(f"distance: {distance}")

            solution.append(mat[cursor[0]][cursor[1]])
            for _ in range(distance):
                cursor = (cursor[0] + direction[0], cursor[1] + direction[1])
                print(f"cursor: {cursor} (directional move)")
                solution.append(matrix[cursor[0]][cursor[1]])
            if direction == UP_RIGHT:
                cursor = (cursor[0], cursor[1]+1) if cursor[1] < n else (cursor[0]+1, cursor[1])
            else:
                cursor = (cursor[0]+1, cursor[1]) if cursor[0] < m else (cursor[0], cursor[1]+1)
            direction = DOWN_LEFT if direction == UP_RIGHT else UP_RIGHT
            if distance == min(n, m):
                decreasing = True
            distance = distance + 1 if not decreasing else distance - 1
            print(f"cursor: {cursor} (adjustment)")
        solution.append(mat[m][n])
        return solution


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
    # ([[1, 2, 3],
    #  [4, 5, 6]],
    # [1, 2, 4, 5, 3, 6]),
    # ([[1, 2],
    #  [3, 4]],
    # [1, 2, 3, 4])
]
for i, case in enumerate(cases):
    matrix, expected = case
    actual = s.findDiagonalOrder(matrix)
    assert actual == expected, f"{i}: {actual} != {expected}"
