"""
In: List[List[Int]] (int are 0 / 1)
Out: Int, number of "corner rectangles"
--------------------------------------
- I worked on this problem in person with a Bradfield friend. We also
looked at the titles of LeetCode problems (but not the associated explanations)
as a clue after we got stuck.
-------------------------------
Strategy for an MxN matrix:
  - counts = {}
  - Go through each row of the matrix doing the following operation; O(M):
  - Finding all possible pairs of 1s (O(N^2)); hash pairs via indices in a tuple to 1,
  or increment it if it has been seen. E.g. if in row 1, both row[2] and row[3] are set,
  we set counts[(2,3)] to 1. If in row 2 we find both row[2] and row[3] are set, we increment
  counts[(2,3)] to 2.
  - Finally, total = 0; for each in counts.keys(), total+= (counts[each]-1*(counts[each]))/2; return total
    - The way to count the number of rectangles is similar to 1+2+3+4...; except here 1 -> 0, 2 -> 1, 3 -> 3, etc.
      1+2+3+4... can be explictly computed with f(n) = n*(n+1)/2. In our case, f(n) = (n-1)*n/2
"""
import collections
import test

class Solution:
    def computeRectangleCount(self, pairCounts):
      total = 0
      for pair in pairCounts.keys():
        pairCount = pairCounts[pair]
        if pairCount > 1:
          total += int(pairCount*(pairCount-1)/2)
      return total

    def countPairs(self, row, pairCounts):
      for left in range(len(row)):
        for right in range(left+1, len(row)):
          if row[left] == row[right] == 1:
            pairCounts[(left,right)] += 1

    def countCornerRectangles(self, grid):
        pairCounts = collections.defaultdict(int)
        for row in grid:
          self.countPairs(row, pairCounts)
        return self.computeRectangleCount(pairCounts)

if __name__ == '__main__':
  s = Solution()
  """
  assert s.countCornerRectangles([[1, 0, 0, 1, 0],
                                  [0, 0, 1, 0, 1],
                                  [0, 0, 0, 1, 0],
                                  [1, 0, 1, 0, 1]]) == 1
  assert s.countCornerRectangles([[1, 1, 1],[1, 1, 1],[1, 1, 1]]) == 9
  assert s.countCornerRectangles([[1, 1, 1, 1]]) == 0
  """
  print(s.countCornerRectangles(test.huge))
