"""
Given a 2D board and a word, find if the word exists in the grid. The word can be
constructed from letters of sequentially adjacent cell, where "adjacent" cells are
those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
----------------------------------
In: List[List[Str]], str
Out: Bool

- We did this problem at Bradfield as an example of backtracking
- In backtracking, we search by doing an exhaustive search where we commit to previous
"moves" that worked (in this case, a move is a selecting a letter on the board)
- If we determine that no subsequent moves from a committed move would produce a solution,
we uncommit and continue searching
- By committing only to viable moves, we take what would've been an exhaustive brute force search
and significantly reduce the amount of work we'd have to do.
-------------------------------------------------------------
pseudo(board, word):
  - class variable visited := empty set
  - class variable board := board
  - loop through all characters looking for word[0]
    - if word[0] is found:
      - add cell to visited
      - pop first letter of word
      - begin backtracking search and return result
  - otherwise return false

backtracking search(word):
  - check each neighboring cell
    - if cell not in visited and contains word[0]:
      - add cell to visited
      - if backtracking search on word(1:) works:
        - return True
      - otherwise, remove the cell from visited and keep looking
  - if no adjacent cell worked, return false
"""


class Solution:
    def __init__(self):
      self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def isValidCell(y, x):
     return 0 <= y < len(self.board) and 0 <= x < len(self.board[0])

    def btSearch(word, cell):
      for y, x in self.directions:
        y += cell[0]
        x += cell[1]
        if self.isValidCell(y, x) and (y, x) not in self.visited and self.board[y][x] == word[0]:
          self.visited.add((y, x))
          if self.btSearch(word[1:], (y, x)):
            return True
          self.visited.remove(y, x)
      return False

    def exist(self, board, word):
        self.board = board
        self.visited = set()
        for y, row in enumerate(board):
          for x, col in enumerate(row):
            if col == word[0]:
              visited.add((y, x))
              if self.btSearch(word[1:]) == True:
                return True
              visited.remove((y, x))
        return False


if __name__ == '__main__':
  s = Solution()
 board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
assert s.exist(board, "ABCCED") == True
assert s.exist(board, "SEE") == True
assert s.exist(board, "ABCB") == False
assert s.exist(board, "") == True


