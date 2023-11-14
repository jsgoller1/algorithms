from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)

        visited = set()

        def valid(y, x):
            return 0 <= y < len(board) and 0 <= x < len(board[0])

        def find(idx, y, x):
            if word[idx] != board[y][x]:
                return False
            if idx+1 == len(word):
                return True
            visited.add((y, x))
            for n_y, n_x in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
                if valid(n_y, n_x) and (n_y, n_x) not in visited:
                    if find(idx+1, n_y, n_x):
                        return True
            visited.remove((y, x))
            return False

        for y, row in enumerate(board):
            for x, c in enumerate(row):
                if find(0, y, x):
                    return True
        return False


s = Solution()
cases = [
    ([["A", "A"]], "AAA", False),
    ([["A"]], "A", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE", True),
    ([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB", False)
]
for board, word, expected in cases:
    actual = s.exist(board, word)
    assert actual == expected, f"{word}: {actual} != {expected}"
