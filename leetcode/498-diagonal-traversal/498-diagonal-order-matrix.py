"""
Start at (0,0), end at (m-1, n-1)
Implement function that triggers move based on last exit point and next direction
    Two move types:
        - up/right: if we're not in the last col, move right. otherwise, down. 
        - down/left: if we're not in the bottom row, move down. otherwise right. 
"""
from typing import List

UP_RIGHT = (-1, 1)
DOWN_LEFT = (1, -1)


class Solution:
    def validCell(self, mat, cell):
        return 0 <= cell[0] < len(mat) and 0 <= cell[1] < len(mat[0])

    def getIdxs(self, mat, startCell, moveDir, idxs):
        while self.validCell(mat, startCell):
            idxs.append(startCell)
            startCell = (startCell[0] + moveDir[0], startCell[1] + moveDir[1])
        return idxs[-1]

    def getStartCell(self, mat, lastCell, moveDir):
        """
        We exited the matrix at lastCell while moving in 
        moveDir. Where do we go next? 
        """
        if moveDir == UP_RIGHT:
            # Move right unless we're in the last column, instead, moving down.
            return (lastCell[0], lastCell[1]+1) if lastCell[1] != len(mat[0])-1 else (lastCell[0]+1, lastCell[1])

        # Move down, unless we're in the bottom row, instead moving right
        return (lastCell[0]+1, lastCell[1]) if lastCell[0] != len(mat)-1 else (lastCell[0], lastCell[1]+1)

    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        idxs = []
        startCell = (0, 0)
        lastCell = None
        moveDir = UP_RIGHT
        while lastCell != (len(mat)-1, len(mat[0])-1):
            lastCell = self.getIdxs(mat, startCell, moveDir, idxs)
            startCell = self.getStartCell(mat, lastCell, moveDir)
            moveDir = DOWN_LEFT if moveDir == UP_RIGHT else UP_RIGHT
        return [mat[y][x] for y, x in idxs]


s = Solution()
for mat, expected in [
    ([[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]], [1, 2, 4, 7, 5, 3, 6, 8, 9]),
    ([[1, 2],
      [3, 4]], [1, 2, 3, 4]),
    ([[1, 2],
      [3, 4],
      [5, 6]], [1, 2, 3, 5, 4, 6]),
    ([[1]], [1])
]:
    actual = s.findDiagonalOrder(mat)
    assert actual == expected, f"{actual} != {expected}"
