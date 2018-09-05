"""
Statment: https://leetcode.com/problems/triangle/description/

Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n)
extra space, where n is the total number of rows in the triangle.
----
Understand

In this problem, we need to find the minimal path from all possible paths
starting at the top node and ending at a bottom node (or vice versa).

In: List of ints
Out: int

----
Plan

Dynamic programming time! Note that at each node, there are two paths, one to each of its children.
One of them is shorter. How do we find the path to that child? Note that to get to it, there are two
paths, one to each of its children. One of them is shorter. (repeat until you hit the ground floor)

There is no situation where we will find a _shorter_ way than we have already found by adding more nodes
(i.e. there are no negative path costs) and we can't go backwards; as such, we don't need to care about
the shortest path to previous floors.

So for an interative solution:
  - starting at the bottom + 1 floor, pick the smaller of the two children and "collapse it" into
    the parent by adding them.
    - if the parent is at array[n][m], the children will be at array[n+1][m] and array[n+1][m+1]
  - Continue this process until we get to the top floor.
  - Return the result, which will be triangle[0][0].

For a recursive one:
  The shortest path to arr[i][j] = min(minimumTotal(arr[i+1][j]), minimumTotal(arr[i+1][j+1]))
  base case is if j = len(triangle) - 1
----
Execute

See below
----
Review

Forthcoming.
"""


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.cache = {}
        self.triangle = triangle
        return self.solve(0, 0)

    def solve(self, floor, child):
        if (floor, child) in self.cache:
            return self.cache[(floor, child)]
        if floor == len(self.triangle) - 1:
            return self.triangle[floor][child]
        shorter = min(self.solve(floor + 1, child),
                      self.solve(floor + 1, child + 1))
        path = self.triangle[floor][child] + shorter
        self.cache[(floor, child)] = path
        return path


if __name__ == '__main__':
    s = Solution()
    assert s.minimumTotal([
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]) == 11
