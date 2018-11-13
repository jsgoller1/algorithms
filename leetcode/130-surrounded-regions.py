"""
Given a 2D board containing 'X' and 'O' (the letter O), capture
all regions surrounded by 'X'.

A region is captured by flipping all 'O's
into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means
that any 'O' on the border of the board are not flipped to
'X'. Any 'O' that is not on the border and it is not connected
to an 'O' on the border will be flipped to 'X'. Two cells are
connected if they are adjacent cells connected horizontally
or vertically.
-----------------------
Input: List[List[str]]
Output: None, modify input in-place

- DFS solution:
  - go through each cell of the board, mantaining visited set
  - if we find an 0, begin a dfs on that cell
    - dfs uses visited set, possible Os and looks for other O cells
    - if the dfs finds a border or cell known to be uncapturable, none of the Os can be converted as
    they are connected to an unsurrounded and by extension none of them are surrounded
    - if no border is found and the dfs is exhausted, convert all Os to Xs
    - using the visited set with the DFS will ensure no cells are visited twice
"""


class Solution(object):
    def surroundDFS(self, y, x, visited, uncapturable, board):
        discovered = set()
        capturable = True
        q = [(y, x)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            currY, currX = q.pop()
            #print("Visiting {0}".format((currY, currX)))
            visited.add((currY, currX))
            discovered.add((currY, currX))
            if not ((1 <= currY < len(board) - 1) and (1 <= currX < len(board[0]) - 1)):
                capturable = False
                continue
            for direction in directions:
                nextY = currY + direction[0]
                nextX = currX + direction[1]
                if board[nextY][nextX] == 'O':
                    if (nextY, nextX) in uncapturable:
                        capturable = False
                    elif (nextY, nextX) not in visited:
                        q.append((nextY, nextX))

        for y, x in discovered:
            if capturable:
                board[y][x] = 'X'
            else:
                uncapturable.add((y, x))

    def solve(self, board):
        visited = set()
        uncapturable = set()
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                if board[y][x] not in visited:
                    if col == "O":
                        self.surroundDFS(y, x, visited, uncapturable, board)
                    else:
                        visited.add((y, x))


if __name__ == '__main__':
    s = Solution()
    tests = [([["X", "X", "X", "X"],
               ["X", "O", "O", "X"],
               ["X", "X", "O", "X"],
               ["X", "O", "X", "X"]], [["X", "X", "X", "X"],
                                       ["X", "X", "X", "X"],
                                       ["X", "X", "X", "X"],
                                       ["X", "O", "X", "X"]]),

             ([["X", "X", "X", "X"],
               ["X", "X", "X", "X"],
               ["X", "X", "X", "X"],
               ["X", "X", "X", "X"]], [["X", "X", "X", "X"],
                                       ["X", "X", "X", "X"],
                                       ["X", "X", "X", "X"],
                                       ["X", "X", "X", "X"]]),
             ([["O", "O", "O", "O"],
               ["O", "O", "O", "O"],
               ["O", "O", "O", "O"],
               ["O", "O", "O", "O"]], [["O", "O", "O", "O"],
                                       ["O", "O", "O", "O"],
                                       ["O", "O", "O", "O"],
                                       ["O", "O", "O", "O"]]),
             ([[]], [[]]),
             ([["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
               ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
                 ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
                 ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
                 ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
                 ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
                 ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
                 ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
                 ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
                 ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]],
                 #
                 [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
                  ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
                  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
                  ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                  ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                  ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
                  ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
                  ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"],
                  ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]),
             ([["O", "X", "O", "O", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
               ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
               ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
               ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
               ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "O", "O", "X", "X", "O", "O"]],
              #
              [["O", "X", "O", "O", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "X"],
               ["O", "X", "O", "X", "O", "O", "O", "O", "X"],
               ["O", "O", "O", "O", "X", "O", "O", "O", "O"],
               ["X", "O", "O", "O", "O", "O", "O", "O", "X"],
               ["X", "X", "O", "O", "X", "O", "X", "O", "X"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "X", "O", "O", "O", "O", "O"],
               ["O", "O", "O", "O", "O", "X", "X", "O", "O"]]
              )]

    for test in tests:
        board = test[0]
        solution = test[1]
        s.solve(board)
        for y, row in enumerate(board):
            for x, col in enumerate(row):
                print("Verifying {0}".format((y, x)))
                try:
                    assert col == solution[y][x]
                except AssertionError:
                    for row in board:
                        print(row)
                    raise AssertionError
