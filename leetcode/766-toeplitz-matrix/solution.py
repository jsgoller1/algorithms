class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        def valid(y: int, x: int):
            return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])

        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if valid(y-1, x-1) and matrix[y-1][x-1] != cell:
                    return False
                if valid(y+1, x+1) and matrix[y+1][x+1] != cell:
                    return False
        return True
