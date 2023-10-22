from collections import deque


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not (matrix and matrix[0]):
            return []

        solution = []
        directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        moves = deque([len(matrix[0]), len(matrix)-1])  # n, m-1

        cursor = (0, -1)
        curr_moves = moves.popleft()

        while 0 < curr_moves:
            direction = directions.popleft()
            for i in range(curr_moves):
                cursor = cursor[0] + direction[0], cursor[1] + direction[1]
                solution.append(matrix[cursor[0]][cursor[1]])
            moves.append(max(curr_moves-1, 0))
            curr_moves = moves.popleft()
            directions.append(direction)
        return solution
