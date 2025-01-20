from collections import deque


class Solution:
    def getNeighbors(self, y, x):
        neighbors = []
        if 0 <= y+1 < len(self.board):
            neighbors.append((y+1, x))
        if 0 <= y-1 < len(self.board):
            neighbors.append((y-1, x))
        if 0 <= x+1 < len(self.board[0]):
            neighbors.append((y, x+1))
        if 0 <= x-1 < len(self.board[0]):
            neighbors.append((y, x-1))
        return neighbors

    def search(self, y, x, visited, idx):
        if self.board[y][x] != self.word[idx]:
            return False
        if idx == len(self.word)-1:
            return True

        # NOTE: If desired, we could instead fill each
        # visited cell with "#" if mutating the board is allowed.
        # This would save time with overhead on set operations.
        for neighbor in self.getNeighbors(y, x):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            if self.search(neighbor[0], neighbor[1], visited, idx+1):
                return True
            visited.remove(neighbor)
        return False

    def exist(self, board, word: str) -> bool:
        self.board = board
        self.word = word

        for y, row in enumerate(board):
            for x, _ in enumerate(row):
                if self.search(y, x, set([(y, x)]), 0):
                    return True
        return False


s = Solution()
for i, case in enumerate([
    ("ABCCED", [["A", "B", "C", "E"], [
     "S", "F", "C", "S"], ["A", "D", "E", "E"]], True),
    ("SEE", [["A", "B", "C", "E"], [
     "S", "F", "C", "S"], ["A", "D", "E", "E"]], True),
    ("ABCB", [["A", "B", "C", "E"], [
     "S", "F", "C", "S"], ["A", "D", "E", "E"]], False),
    ("A", [["A"]], True)
]):
    word, board, expected = case
    actual = s.exist(board, word)
    assert actual == expected, f"{i}: {actual} != {expected}"
