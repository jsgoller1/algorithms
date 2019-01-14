"""
average case:
[
  [10, 5, 4, 9, 10],
  [2, 6, 8, 5, 5],
  [7, 2, 0, 7, 7],
  [4, 2, 9, 8, 2],
  [8, 10, 2, 4, 4]
]
Solution:
[
  [P, P, P, P, PA],
  [P, P, P, 5, 5],
  [P, 2, 0, 7, 7],
  [4, 2, 9, 8, 2],
  [8, 10, 2, 4, 4]
]



all case:
[
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5],
  [5, 5, 5, 5, 5]
]
---------------------------------
- Graph; cells are nodes, directed edge from cell A to cell B exist if height(A) > height(B);
  undirected edge exists if equal
- For each cell, determine if water can flow from that cell to both oceans; return
  cells where this is true for both
- If we're on row/col 0, we can reach the atlantic ocean
- If we're on row len(matrix)-1 or col len(matrix[0])-1, we can reach the atlantic
- If we can reach a cell that can reach an ocean, we can reach an ocean

- Can we use a DFS/BFS for this?
  - The DFS should look at "all places water can flow here from" (higher neighbors), but this is problematic
    for cases of equal height
  - A brute force approach is to launch a DFS from every possible cell and see if we can hit any ocean, and then back
    propagate the result. This results in unnecessary effort.
  - What about:
    - Keep a separate visited set
    - Loop over every cell
      - If it's on a border, add its respective oceans to the ocean set
      - For every neighbor, if a neighboring cell is lower:
        - if unvisited, visit it and add it to visited
        - copy its ocean set
    - Then loop over ever cell again:
      - if its ocean set is PA, add it to the solution
------------------------------------

"""
import collections


class Solution(object):
    def __init__(self):
        self.directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def isValid(self, matrix, cell):
        y, x = cell
        return 0 <= y < len(matrix) and 0 <= x < len(matrix[0])

    def dfs(self, matrix, cell, visited, accessible):
        # print("Visiting: {0}".format(cell))
        visited.add(cell)
        y, x = cell
        if y == 0 or x == 0:
            accessible[cell].add('P')
        if y == len(matrix) - 1 or x == len(matrix[0]) - 1:
            accessible[cell].add('A')

        for direction in self.directions:
            neighborY, neighborX = y + direction[0], x + direction[1]
            neighbor = (neighborY, neighborX)
            if self.isValid(matrix, neighbor) and matrix[y][x] >= matrix[neighborY][neighborX]:
                if neighbor not in visited:
                    self.dfs(matrix, neighbor, visited, accessible)
                accessible[cell].update(accessible[neighbor])

    def pacificAtlantic(self, matrix):
        visited = set()  # might be able to just use accessible for this
        accessible = collections.defaultdict(set)
        for y, row in enumerate(matrix):
            for x, cell in enumerate(row):
                if (y, x) not in visited:
                  self.dfs(matrix, (y, x), visited, accessible)
        for key in accessible:
          if key in [(10,3), (12,3), (11,2), (11,4)]:
            print("{0}: {1}".format(key, accessible[key]))

        return [[key[0], key[1]] for key in accessible if accessible[key] == set(['P', 'A'])]


if __name__ == '__main__':
    cases = [
        ([[3, 3, 3, 3, 3, 3],
          [3, 0, 3, 3, 0, 3],
          [3, 3, 3, 3, 3, 3]], [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [1, 0], [1, 2], [1, 3], [1, 5], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5]]),
        ([[7,1,17,13,9,10,5,14,0,3],[7,15,7,8,15,16,10,10,5,13],[18,9,15,8,19,16,7,5,5,10],[15,11,18,3,1,17,6,4,10,19],[3,16,19,12,12,19,2,14,5,9],[7,16,0,13,14,7,2,8,6,19],[5,10,1,10,2,12,19,1,0,19],[13,18,19,12,17,17,4,5,8,2],[2,1,17,13,14,12,14,2,16,10],[5,8,1,11,16,1,18,15,6,19],[3,8,14,14,5,0,2,7,5,1],[17,1,9,17,10,10,10,7,1,16],[14,18,5,11,17,15,8,8,14,13],[6,4,10,17,8,0,11,4,2,8],[16,11,17,9,3,2,11,0,6,5],[12,18,18,11,1,7,12,16,12,12],[2,14,12,0,2,8,5,10,7,0],[16,13,1,19,8,13,11,8,11,3],[11,2,8,19,6,14,14,6,16,12],[18,0,18,10,16,15,15,12,4,3],[8,15,9,13,8,2,6,11,17,6],[7,3,0,18,7,12,2,3,12,10],[7,9,13,0,11,16,9,9,12,13],[9,4,19,6,8,10,12,6,7,11],[5,9,18,0,4,9,6,4,0,1],[9,12,1,11,13,13,0,16,0,6],[7,15,4,8,15,17,17,19,15,1],[7,17,4,1,1,14,10,19,10,19],[10,5,12,5,8,8,14,14,6,0],[16,10,10,7,13,4,0,15,18,0],[11,2,10,6,5,13,4,5,3,1],[9,14,16,14,15,3,2,13,17,8],[19,2,10,1,2,15,12,10,2,5],[12,4,8,9,8,6,4,14,14,0],[11,17,17,4,16,13,6,15,5,7],[12,18,1,3,9,10,7,1,1,1],[18,6,10,8,12,14,9,12,10,3],[15,13,18,13,8,5,12,14,18,0],[15,4,8,9,19,18,6,19,12,0],[4,14,15,4,17,17,9,17,9,0],[6,17,16,10,3,8,8,18,15,9],[3,8,4,2,13,0,2,8,8,2],[14,12,13,12,17,4,16,9,8,7],[0,19,8,16,1,13,7,6,15,11],[1,13,16,14,10,4,11,19,9,13],[8,0,2,1,16,12,16,9,9,9],[5,2,10,4,8,12,17,0,2,15],[11,2,15,15,14,9,11,19,18,11],[4,4,1,5,13,19,9,17,17,17],[4,1,8,0,8,19,11,0,5,4],[8,16,14,18,12,2,0,19,0,13],[7,11,3,18,8,2,2,19,8,7],[3,13,6,1,12,16,4,13,0,5],[12,1,16,19,2,12,16,15,19,6],[1,7,12,15,3,3,13,17,16,12]],[[0,9],[1,9],[2,9],[3,9],[11,3],[53,0],[53,2],[53,3],[54,0],[54,1],[54,2],[54,3]])
    ]
    s = Solution()
    for case in cases:
        print("--"*15)
        landmap = case[0]
        for i, row in enumerate(landmap):
          print("{0}: {1}".format(i,row))
        expected = case[1]
        actual = s.pacificAtlantic(landmap)
        actualSet = set([tuple(cell) for cell in actual])
        expectedSet = set([tuple(cell) for cell in expected])
        print("Need: {0}".format(expectedSet.difference(actualSet)))
        print("Wrong: {0}".format(actualSet.difference(expectedSet)))
        assert actualSet == expectedSet
