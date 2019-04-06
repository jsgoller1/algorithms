"""
Given an integer matrix, find the length of the longest
increasing path. From each cell, you can either move to
four directions: left, right, up or down. You may NOT
move diagonally or move outside of the boundary
(i.e. wrap-around is not allowed).

Example 1:

Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
------------------------------------------
Input: list[list[int]]
Output: int

- we are trying to find the longest _strictly increasing_ path in the given matrix.
- How many times do we actually need to look at every element in the matrix?
  - Can we do it just once?
  - Is there a way we can disqualify a cell once we visit it?
- What about a topological sort?
  - A topological ordering can be constructed by saying a cells comes "before" another cell
  iff it is adjacent and lower in value
  - If there are multiple paths in the matrix, will a top order still work?
  - we can construct a topologial order data structure in O(n) time; but how quickly can we determine tbe longest path?
- A heap / priority queue can allow us to retrieve minimal / maximal things; could we put cells
  into a pq?
- What about backtracking?
  - We can use our BFS / DFS approach and then back out of bad paths with backtracking
    - backtracking (i think) would be better if we were "searching" for some kind of answer;
    although we are searching for a longest path, we don't necessarily know when we've found it
    until we know there's no other possible paths.
- Can we use a DP approach?
  - Calculate longest path in 1x1 then 2x2 then 3x3 until we have the whole matrix?
  - Say we start with matrix A:
      [1, 2]
      [1, 3]
  - We can see that the longest path is 1-2-3. Now, if we add another column to create
    matrix B, we might get:
      [1, 2, 7]
      [1, 3, 8]
  - Now there are two longest paths (1-2-7-8 and 1-2-3-8). Can this fact about B be easily inferred
  from A?
    - It is possible that in adding a new row / col we might:
      - Add a new cell from which a path could begin
      - add a new cell at which a path could end
      - Add an entirely new path
      - This probably won't work any more efficiently than quadratic time
  - A brute-force approach is to attempt a BFS/DFS from every cell in the matrix;
    - This would work but would be O((n*m)^2)
    - If we BFS/ DFS, we should not need to visit any cell more than once.
    - Suppose we start with the entire matrix; we can recursively DFS until we find no more cells
    to visit; if this is the case, set to 1. When we return, set to 1 + highest visitable neighbor
--------------------------------------------------------------------------------------
- DFS with caching approach
- Create a separate matrix $costs that is the same size as $input, but all set to 0
- Go through every row/col in $input; if cost[row][col] != 0, skip it (i.e. it's been visited)
- Otherwise, begin dfs from that cell.
  - The DFS's base case is that the cell has no visitable neighbors; if so, set costs[row][col] to 1
  - Otherwise visit all neighbors; then, set the current cell's costs to 1+max neighbor.
- As we run the program, we can also keep track of a global maximum; each time we set the value of a cell,
set the global max to max(cell's cost, current max); then at the end return the global max
- Overall running time is linear, as is space use.
  - Because it's a recursive function, we are going to wind up with linear space no matter what.
  - Using a stack to hold node values would also be linear space
----------------------------------------------------------------------------------------
Review:
  - First attempt initially failed because implementation checks for 0 to see if a cell
  can be visited and does full UDLR sweep during DFS, meaning that we are ping-ponging between
  two cells; is it too risky to instead initialize our pathLengths dict with None, then set it to
  0 if we've already visited but don't know the path cost, but then set it to 1 or greater once we know
  the path cost?
"""


class Solution(object):
    def __init__(self):
        # TODO:  do we need left and up?
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def isValidCell(self, *, y, x):
        validY = 0 <= y < len(self.matrix)
        validX = 0 <= x < len(self.matrix[0])
        return validX and validY

    def wasVisited(self, *, y, x):
        return self.longestPathLength[y][x] != 0

    def isIncreasingPath(self, *, currY, neighborY, currX, neighborX):
        return self.matrix[currY][currX] < self.matrix[neighborY][neighborX]

    def getMaxNeighborPathLength(self, *, y, x):
        maxLength = 0
        for direction in self.directions:
            neighborY = y + direction[0]
            neighborX = x + direction[1]
            if self.isValidCell(y=neighborY, x=neighborX) and self.isIncreasingPath(currY=y, neighborY=neighborY, currX=x, neighborX=neighborX):
                maxLength = max(
                    maxLength, self.longestPathLength[neighborY][neighborX])
        return maxLength

    def dfs(self, *, y, x):
        self.longestPathLength[y][x] = 1
        for direction in self.directions:
            neighborY = y + direction[0]
            neighborX = x + direction[1]
            if self.isValidCell(y=neighborY, x=neighborX) and not self.wasVisited(y=neighborY, x=neighborX) and self.isIncreasingPath(currY=y, neighborY=neighborY, currX=x, neighborX=neighborX):
                self.dfs(y=neighborY, x=neighborX)

        self.longestPathLength[y][x] += self.getMaxNeighborPathLength(
            y=y, x=x)
        self.globalLongestPath = max(
            self.globalLongestPath,  self.longestPathLength[y][x])

    def longestIncreasingPath(self, matrix):
        self.matrix = matrix
        self.longestPathLength = [[0 for col in matrix[0]] for row in matrix]
        self.globalLongestPath = 0
        for y, row in enumerate(matrix):
            for x, col in enumerate(matrix[y]):
                if self.longestPathLength[y][x] == 0:
                    self.dfs(y=y, x=x)
        return self.globalLongestPath


if __name__ == '__main__':
    s = Solution()
    testCases = [
        ([[3, 4, 5],  # normal case
          [3, 2, 6],
          [2, 2, 1]],
         4),
        ([[9, 8, 7],  # upward, every element of array is used
          [4, 5, 6],
          [3, 2, 1]],
         9),
        ([[1, 2, 3],  # downward, every element of array is used
          [6, 5, 4],
          [7, 8, 9]],
         9),
        ([[1, 1, 1],  # no element is used
          [1, 1, 1],
          [1, 1, 1]],
         1),
        ([[]],  # null case
         0),
    ]
    for case in testCases:
        maze = case[0]
        length = case[1]
        for row in maze:
            print(row)
        assert s.longestIncreasingPath(maze) == length
        print("="*25)
