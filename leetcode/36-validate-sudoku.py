"""
I copied and pasted this from 37-sudoku-solver.py; see
that file for notes.
"""


class Solution:
    def isValidSudoku(self, board):
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
