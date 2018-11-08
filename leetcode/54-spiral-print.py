"""
Given a matrix of m x n elements (m rows, n columns), return
all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Input: List[List[Int]]
Output: List[Int]

Constraints:
  - None given
-----------------------
- Ah, spiral print; the problem that made Asana turn me down. Hello,
darkness, my old friend...

- One (particularly error prone) approach is the "sentinel values" approach. Something like:
  set top, left, right, and bottom to be the "furthest valid indices"
  starting with top left, print:
    - every entry in the top row from left to right, the increment the row
    - every entry in the rightmost column from top to bottom, then decrement right
    - every entry in the bottom row from right to left, then decrement bottom
    - every entry in left from bottom to top, then increment left
  - do this while:
    - the left column index is less than the right
    - bottom row index is less than top
- Notice though that for an N X N matrix, we will visit N, N-1, N-1, N-2, N-2, N-3, N-3,...1,1 cells.
  For:
  1 2 3
  4 5 6
  7 8 9

  The spiral print is
  1 2 3 6 9 8 7 4 5
  or
  1 2 3
  6 9
  8 7
  4
  5
- For an N x M where N != M, the pattern is N, M-1, N-1, M-2, N-2, ... 0.
- If we started with a "cursor" at 0,0 and a list of "directions" right = (0,1), left = (0, -1), and so on,
we can go through each number of cells in our N, N-1, N-1...1,1 sequence and visit that many cells. Here's an approach
based on that:
  #                 L       D     R       U
  - directions = [(0,1), (1,0), (0,-1), (-1,0))]
  - spiral = []
  - cursor = (0,0)
  - moves, prevMoves = len(matrix[0]), None
  - while moves > 0:
    - direction = directions.popleft()
    - pick next direction, move cursor $moves many cells in that direction appending entries to $spiral
    - directions.append(direction)
    - if moves == prevMoves:
      moves = prevMoves-1
    - else:
      prevMoves = moves
"""

import collections

class Solution:
    def spiralOrder(self, matrix):
        if matrix == []:
          return matrix
        directions = collections.deque([(0,1), (1,0), (0,-1), (-1,0)])
        spiral = []
        cursor = [0,-1]
        moves, nextMoves = len(matrix[0]), len(matrix)-1
        while moves > 0:
          direction = directions.popleft()
          for _ in range(moves):
            cursor[0] += direction[0]
            cursor[1] += direction[1]
            spiral.append(matrix[cursor[0]][cursor[1]])
          directions.append(direction)
          nextMoves, moves = moves-1, nextMoves
        return spiral


if __name__ == '__main__':
    s = Solution()
    assert s.spiralOrder([[]]) == []
    assert s.spiralOrder([[1, 2, 3, 4]]) == [1, 2, 3, 4]
    assert s.spiralOrder([[1], [2], [3], [4]]) == [1, 2, 3, 4]
    assert s.spiralOrder([
         [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]
     ]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert s.spiralOrder([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
