"""
Given a square array of integers A, we want the minimum sum of a falling path through A.
A falling path starts at any element in the first row, and chooses one element from each
row. The next row's choice must be in a column that is different from the previous row's
column by at most one.

Example 1:
Input: [[1,2,3],
        [4,5,6],
        [7,8,9]]
Output: 12
Explanation:
The possible falling paths are:
[1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
[2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
[3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
The falling path with the smallest sum is [1,4,7], so the answer is 12.

Note:
1 <= A.length == A[0].length <= 100
-100 <= A[i][j] <= 100
-----------------------------------------------
In: list[list[int]]
Out: int
- will be at most a 100 x 100 array
- values between -100 and 100

- Don't need to keep track of WHICH path, just how much THE path costs

- Brute force: dfs
  - Each col i in row j can be a node, and has edges to col i-1, i+1, and i in row j+1;
  - We can DFS until we find the minimum path cost
- Alternative: "roll forward"
  - for each column i in row j, add to it min(i-1, i, i+1) from row j-1. This way, we know the minimal cost
  associated with reaching any given cell. Then, just select the minimum from row len-1.
-------------------------------------------------
roll_forward(matrix):
  if len matrix == 0:
    return 0
  if len matrix == 1:
    return min of first row
  else:
    set i to 1
    for each index j in row i:
      set matrix[i][j] to min of row[i-1][j-1,j,j+1]
    i++
    return min of last row
"""

class Solution(object):
    def minFallingPathSum(self, matrix):
        if len(matrix) == 0:
          return 0
        if len(matrix) == 1:
          return min(matrix[0])

        y = 1
        while y < len(matrix):
          for x, _ in enumerate(matrix[y]):
            left = max(x-1, 0)
            right = min(x+1, len(matrix[0])-1)
            matrix[y][x] += min([matrix[y-1][left], matrix[y-1][x], matrix[y-1][right]])
          y += 1
        return min(matrix[-1])

if __name__ == '__main__':
  s = Solution()
  assert s.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 12
  assert s.minFallingPathSum([]) == 0
  assert s.minFallingPathSum([[1,1,1],[1,1,1],[1,1,1]]) == 3

