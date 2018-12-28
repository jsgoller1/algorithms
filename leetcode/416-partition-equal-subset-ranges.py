"""
Given a non-empty array containing only positive integers, find if the
array can be partitioned into two subsets such that the sum of elements
in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
------------------------------------------------------------------------
- This problem is called the linear partition problem; I read the wikipedia
page for it because I was attempting to understand a variant given by Skiena
in the dynamic programming chapter of the algorithm design manual (n-many
partitions instead of 2, but a string of ints where order must be maintained
instead of aribtrary sets).

- Intuition for the algorithm
  - Let K be the sum of our set S, where K = s1 + s2 + s3 ... + sn for all S in s.
  - Suppose we had a function, f(i,j) that determines if s1 + s2 + s3...+ sj = i.
    Our task in this problem is to determine f(K/2, N) where N is the size of S.
  - f(i,j) returns true under two conditions, false otherwise:
    - if f(i,j-1) is True, so is f(i,j) (some subset of this set sums to i)
    - if f(i-xj,j-1) is True, then a previous subset sums to an amount out of which we can
    make i by adding the last element of our set. Example - if our set is {1,2,3} and i is 6,
    f(6,3) returns true because 1+2 sum to 3 (which is f(6-3, 2)), and 3 + 3 is 6.
  - One confusion I had about his algorithm is that it didn't make sense that the order
    we went from left to right since the elements in a set irrelevant. For instance, what
    happens if we have {1,1,3,3}? and the correct division is picking the middle {1,3} and
    the outer {1,3}?
    - However, remember that we're looking for K/2; if we can find a subset anywhere that
      equals half of the sum of all elements, then the complement (which can come from anywhere
      in any order) will equal the other K/2.
    - Additionally if K is odd, we have two options:
      - Refuse to evaluate because no two sets will ever be equal, and immediately return false
      - Go with floor(k/2) instead.

- Algorithm
  - K = sum of set S
  - DP = a matrix with |S|+1 many columns, and K/2 many rows; the rows are sums we want to make
  and the columns are offsets in our set (representing subets)
    - +1 for the empty set
    - the first column of every row is False, except the first; except 0,
      we cannot make any values from the empty set
    - the first row of every column is also true; because we can make the empty set,
      we can always sum to 0
  - for every cell i,j in the matrix:
      - set it to True if matrix[i][j-1] or matrix[i-set[j], j-1] is True
      - otherwise (including if i-set[j] < 0)
--------------------------------------------------------------------------
- Algorithm works for 50% of cases, but TLEs
- Are we doing work we don't need to be doing?
- Do we necessarily need to fill the entire DP table?
- After trying two different approaches, only sorting appears to
make any positive impact
"""


class SolutionTLE:
    """
    Bottom-up approach as described above; this TLEs after about half
    the test cases, but currently clears the most of them.
    """

    def canPartition(self, nums):
        k = sum(nums)
        nums.sort()
        half = int(k/2)
        if k % 2 != 0 or len(nums) < 2:
            return False
        dp = [[True for elem in nums]] + [[False for elem in nums]
                                          for i in range(half)]
        for y in range(1, half + 1):
            for x in range(1, len(nums)):
                dp[y][x] |= dp[y][x - 1]
                if y - nums[x] >= 0:
                    dp[y][x] |= dp[y - nums[x]][x-1]

        return dp[-1][-1]


class SolutionTLE2:
    """
    Top down, "solve as needed" approach.
    """

    def canPartition(self, nums):
        k = sum(nums)
        half = int(k/2)
        if k % 2 != 0 or len(nums) < 2:
            return False
        self.nums = nums
        self.dp = [[True for elem in nums]] + \
            [[False] + ([None]*(len(nums)-1)) for each in range(half+1)]
        return self.partitionable(half, len(nums)-1)

    def partitionable(self, i, j):
        #print("solving dp[{0}][{1}]".format(i, j))
        if self.dp[i][j] == None:
            self.dp[i][j] = self.partitionable(i, j - 1)
            if i - self.nums[j] >= 0:
                self.dp[i][j] |= self.partitionable(i - self.nums[j], j-1)
        return self.dp[i][j]


class Solution:
    """
    Top down O(c) approach, but this didn't work after even 11s without caching,
    and still only got 85/105 test cases after implementing caching
    """

    def canPartition(self, nums):
        k = sum(nums)
        #nums.sort(reverse=True)
        half = int(k/2)
        if k % 2 != 0 or len(nums) < 2:
            return False
        self.nums = nums
        return self.partitionable(half, len(nums)-1, {})

    def partitionable(self, i, j, cache):
        if (i, j) not in cache:
          if i < 0:
              return False
          if j == 0:
              return i == 0
          cache[(i,j)] = self.partitionable(i, j - 1, cache) or self.partitionable(i - self.nums[j], j-1, cache)
        return cache[(i,j)]


if __name__ == '__main__':
    s = Solution()
    assert s.canPartition([1, 5, 11, 5]) == True
    assert s.canPartition([1, 2, 3, 5]) == False
    assert s.canPartition([61,96,15,73,64,57,7,25,52,68,59,53,72,6,22,76,12,8,29,99,1,77,57,39,95,51,44,61,67,35,70,96,46,91,51,38,33,80,45,68,20,9,6,74,4,89,10,58,95,38,85,62,13,23,2,5,73,45,17,3,62,64,65,50,21,30,36,60,43,57,25,63,47,72,35,94,79,88,2,57,60,32,96,66,90,5,48,74,45,88,24,3,38,80,50,45,83,66,74,91]) == True
    s.canPartition([22,8,19,30,86,46,66,74,93,66,73,58,6,3,44,10,21,4,76,100,65,11,30,87,50,39,53,51,97,60,1,2,25,66,67,87,89,13,64,63,81,80,94,5,20,75,74,80,56,32,54,75,19,28,80,25,59,96,1,12,100,81,49,33,90,13,83,31,77,41,58,64,39,62,100,42,49,43,73,90,85,72,21,79,75,79,43,88,33,98,5,27,45,24,83,53,65,65,63,100])
    assert s.canPartition([]) == False
