"""
While working on LeetCode #37 (sudoku solver), my program kept timing out on the last test case.
I thought I could be clever and implement a randomized search like Skiena demonstrates for quicksort
in the Algorithm Design Manual to circumvent pathological sudoku boards, but it fails to work for
hard cases (I started the program like 10 minutes ago and it still isn't finished). There are
solutions to all LeetCode cases, so I should rethink my approach.
"""
import random
import collections


class Solution:
    def valid(self, board):
        # rows
        for row in board:
            row_set = set()
            for item in row:
                if item in row_set:
                    return False
                elif item != '.':
                    row_set.add(item)

        # columns
        for i in range(9):
            col_set = set()
            for row in board:
                if row[i] in col_set:
                    return False
                elif row[i] != '.':
                    col_set.add(row[i])

        # 3x3s
        square_starts = [0, 3, 6]
        for y in square_starts:
            for x in square_starts:
                square_set = set()
                for i in range(3):
                    for j in range(3):
                        if board[y + i][x + j] in square_set:
                            return False
                        elif board[y + i][x + j] != '.':
                            square_set.add(board[y + i][x + j])
        return True

    def solve(self, board, searchOrder):
        if not searchOrder and self.valid(board):
            return True

        row, col = searchOrder[0] // 9, searchOrder[0] % 9
        temp = searchOrder.popleft()
        if board[row][col] != '.':
            return self.solve(board, searchOrder)
        else:
            for val in range(1, 10):
                board[row][col] = str(val)
                if self.valid(board) and self.solve(board, searchOrder):
                    return True
            board[row][col] = '.'
        searchOrder.appendleft(temp)

    def solveSudoku(self, board):
        searchOrder = collections.deque([i for i in range(81)])
        random.shuffle(searchOrder)
        self.solve(board, searchOrder)


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
    mediumBoard = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    hardBoard = [
        [".", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", ".", ".", ".", ".", "."],
        [".", ".", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", ".", ".", ".", ".", "3"],
        [".", ".", ".", "8", ".", "3", ".", ".", "."],
        [".", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", ".", "."],
        [".", ".", ".", "4", ".", "9", ".", ".", "."],
        [".", ".", ".", ".", "8", ".", ".", "7", "."]]
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
    s.solveSudoku(hardBoard)
    for row in hardBoard:
        print(row)
    assert hardBoard == solvedBoard
    #assert s.solveSudoku(solvedBoard) == True
    #assert s.solveSudoku(solvedBoardInvalid) == False
    #assert s.solveSudoku(validBoard) == True
    #assert s.solveSudoku(invalidBoard) == False
