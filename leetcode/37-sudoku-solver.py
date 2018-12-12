"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
- Each of the digits 1-9 must occur exactly once in each row.
- Each of the digits 1-9 must occur exactly once in each column.
- Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
- Empty cells are indicated by the character '.'

Constraints:
- The given board contain only digits 1-9 and the character '.'.
- You may assume that the given Sudoku puzzle will have a single unique solution.
- The given board size is always 9x9.
-------------------------------------------------------------------

- There are (n^2)^10 (roughly 23 billion for a 9x9 board) possible combinations for this sudoku board
- We solved this during Bradfield, for the backtracking section
- in a nxn board, we can assign each cell to an int between 0 and n^2; we can convert this int back to the
cell coords with (cell_no // n, cell_no % n)
----------------------------------------------

valid(full_board):
  - go through each row:
    - if any duplicates, return False
  - go through each column:
    - if any duplicates, return False
  - go through each 3x3 box:
    - if any duplicates, return False
  - return True

solve(board, cell_id):
      - row, col = cell_id // 9, cell_id % 9
      - if cell_id == 81:
        - return valid(board)
      - if board[row][col] != '.':
        - solve(board, cell_id + 1)
      - else:
        - for each int from 1 to 9:
          - set board[row][col] to the next int
          - if validate(board) and solve(board, cell_id+1)
            - return True
        - set current cell to '.' # return falls through
      - return False

sudoku_solve(board):
  return solve(board, 0)
"""


class Solution:
    def valid(self, board):
        # rows
        for row in board:
            row = [item for item in row if item != '.']
            if len(set(row)) != len(row):
                #print("Invalid row: {0}".format(row))
                return False

        # columns
        for i in range(9):
            column = [row[i] for row in board if row[i] != '.']
            if len(column) != len(set(column)):
                #print("Invalid column: {0}".format(column))
                return False

        # 3x3s
        square_starts = [0, 3, 6]
        for y in square_starts:
            for x in square_starts:
                square = [board[y + i][x + j]
                          for i in range(3) for j in range(3) if board[y + i][x + j] != '.']
                if len(square) != len(set(square)):
                    #print("Invalid square: {0}".format(square))
                    return False
        return True

    def solve(self, board, cell_id):
        if cell_id == 81 and self.valid(board):
            return True

        row, col = cell_id // 9, cell_id % 9
        if board[row][col] != '.':
            return self.solve(board, cell_id + 1)
        else:
            for val in range(1, 10):
                board[row][col] = str(val)
                if self.valid(board) and self.solve(board, cell_id + 1):
                    return True
            board[row][col] = '.'

    def solveSudoku(self, board):
        self.solve(board, 0)


if __name__ == '__main__':
    s = Solution()
    easyBoard = [
        [".", "3", "4", "6", "7", "8", ".", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", ".", "7"],
        ["8", "5", "9", "7", ".", "1", "4", "2", "3"],
        [".", "2", ".", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", ".", "6"],
        ["9", "6", "1", "5", "3", "7", ".", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", ".", "2", "8", ".", "1", "7", "."]
    ]
    validBoard = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    invalidBoard = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    solvedBoard = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    solvedBoardInvalid = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "6", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "3"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    s.solveSudoku(easyBoard)
    assert easyBoard == solvedBoard
    #assert s.solveSudoku(solvedBoard) == True
    #assert s.solveSudoku(solvedBoardInvalid) == False
    #assert s.solveSudoku(validBoard) == True
    #assert s.solveSudoku(invalidBoard) == False
