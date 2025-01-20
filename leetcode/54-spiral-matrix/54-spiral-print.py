UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        moves = [len(matrix[0]), len(matrix)-1]  # w, h
        directions = [RIGHT, DOWN, LEFT, UP]
        idx = 0
        cursor = [0, -1]
        while moves[idx % 2]:
            y, x = directions[idx]
            for i in range(moves[idx % 2]):
                cursor[0] += y
                cursor[1] += x
                order.append(matrix[cursor[0]][cursor[1]])
            moves[idx % 2] -= 1
            idx = (idx + 1) % 4
        return order
