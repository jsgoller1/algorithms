"""
Given an n x m matrix, if an element is 0, set its entire row and column to zero; do this in place.

Example:
1 1 1     1 0 1
1 0 1  -> 0 0 1
1 1 1     1 0 1

In: array of array of ints
Out: array of array of ints with rows zeroed where appropriate

Constraints:
  - Not stated; assuming all entries are ints

Notes:
- A straightforward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space; still not optimal.
- Can you devise a O(c) space solution?
-----------------------------------------
- The O(m*n) approach is probably the best one; create a new
array, modify it as we walk the old array by zeroing if the existing
cell or UDLR neighbor is 0, return the new one
- The O(m+n) approach takes two passes; one to collect all rows / cols which require zeroing,
and another to zero them
- For O(c), could we go through the array and set the values to a third special type, like None?
On pass 1, if any entry is zero, go into a subprocedure that sets that entire row and column to None;
then once we've walked the entire array, set all Nones to zero?
  - We can't just zero on the first pass because then the entire matrix becomes zero.
---------------------------------------
procedure:
  - for y, row in matrix:
    - for x, col in matrix:
      - if col == 0:
        - set everything in row y and column x to None
  - for y, row in matrix:
    - for x, col in matrix:
      if col == None:
          - matrix[y][x] = 0
  return matrix

O(c) space; no extra storage used
O(n*m) time; we will see each matrix entry at most twice
-------------------------
"""

class Solution:
  def zeroLock(self, y, x, matrix):
    for i, row in enumerate(matrix):
      if row[x] != 0:
        matrix[i][x] = None

    for j, colVal in enumerate(matrix[y]):
      if colVal != 0:
        matrix[y][j] = None

  def setZeroes(self, matrix):
    for y, row in enumerate(matrix):
      for x, col in enumerate(row):
        if col == 0:
          self.zeroLock(y,x, matrix)

    for y, row in enumerate(matrix):
      for x, col in enumerate(row):
        if col == None:
          matrix[y][x] = 0

if __name__ == '__main__':
  s = Solution()
  """
  assert s.setZeroes([[]]) == [[]]
  assert s.setZeroes([[0]]) == [[0]]
  assert s.setZeroes([[1, 1, 1],
                      [1, 0, 1],
                      [1, 1, 1]]) == [[ 1, 0, 1],
                                     [0, 0, 0],
                                     [1, 0, 1]]
  assert s.setZeroes([[0, 1, 0],
                      [1, 1, 1],
                      [1, 1, 1]]) == [[ 0, 0, 0],
                                     [0, 1, 0],
                                     [0, 1, 0]]
  assert s.setZeroes([[0,0,0,5],
                      [4,3,1,4],
                      [0,1,1,4],
                      [1,2,1,3],
                      [0,0,1,1]]) == [[0,0,0,0],
                                      [0,0,0,4],
                                      [0,0,0,0],
                                      [0,0,0,3],
                                      [0,0,0,0]]
  """
