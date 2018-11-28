"""
Given an array nums of n integers, are there elements a, b, c in nums such
that a + b + c = 0? Find all unique triplets in the array which gives the
sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
==========================================================================
In: list[int]
Out: list[list[int]]

- During execution, we can store a set of tuples to avoid duplicate elements,
then at the end convert to a list of lists
- Worst possible case is test every possible set of triplets, which is O(n^3).
Can we do better?
- Two-sum is an O(n^2) problem that we can reduce to O(n) with the two pointer approach.
- Is there some way we could do the two-sum O(n) approach, but "for every element
in the array" to find a third element, giving us O(n^2)?
- I have heard people talk about this as a common dynamic programming problem
  - Is the solution composed of solutions to subproblems?
  - Do these subproblems overlap?
- Note that for an arr of len(n), all triplets can be reused for an arr
of len(n+1). So the question is:
  - What is the base case?
    - Probably a len(3) arr
  - What do we do for each n+1 case?
==========================================================================


- start with an empty set (that will store tuples)
- sort the input array
- base case is a 3-element array; if the sum equals target, add it
- for each index k from arr[3] to arr[n-1]:
  - execute modified 2 sum procedure from 0 to k-1, adding arr[k]
    - if total sum == target, add triplet as a tuple to set
- finally at the end, convert the set of tuples to a list of lists and return

- modified 2-sum procedure, with arg k:
  - i = 0, j = 1
  - while i < j:
    - if arr[i] + arr[j] + arr[k] <= target:
"""


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return []


if __name__ == '__main__':
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    assert s.threeSum([-7, -6, -4, -3, 10]) == [
        [-7, -3, 10],
        [-6, -4, 10]
    ]
