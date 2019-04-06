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
    - tripleSum = if arr[i] + arr[j] + arr[k]
    - tripleSum == target:
      store arr[i],arr[j],arr[k]
      i++
      j--
    - elif tripleSum > target:
      j--
    - else
      i++

- in the twosum procedure, we should modify both indices on a match. Suppose
we were only modifying one index, say i. the only way that the new i would match
the old j is if the new i was equal to the old i, which is necessarily a duplicate.
--------------------------
-  Initial run worked on all cases except [0,0,0,...,0], which timed out.
- What if we tried pre-processing by converting nums to a set? Will need additional work
  if every element in the array is the same, but should speed things up.
- Preprocess by conversion to a set. If the length of the set is less than 3, add one of every
element of the set to the array until it isn't.
"""

import collections


class Solution:
    def twoSumPlusK(self, *, nums, triplets, k):
        start = 0
        end = k - 1
        while start < end:
            if nums[start] + nums[end] + nums[k] == 0:
                triplets.add((nums[start], nums[end], nums[k]))
                start += 1
                end -= 1
            elif nums[start] + nums[end] + nums[k] > 0:
                end -= 1
            else:
                start += 1

    def preprocess(self, nums):
        counts = collections.Counter(nums)
        processedNums = []
        for key in counts:
            processedNums += [key] * min(3, counts[key])
        return sorted(processedNums)

    def threeSum(self, nums):
        if len(nums) < 3:
            return []

        nums = self.preprocess(nums)
        triplets = set()
        for k in range(2, len(nums)):
            self.twoSumPlusK(nums=nums, triplets=triplets, k=k)
        print([[item for item in triplet] for triplet in triplets])
        return [[item for item in triplet] for triplet in triplets]


if __name__ == '__main__':
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [
        [-1, -1, 2],
        [-1, 0, 1]
    ]
    assert s.threeSum([-7, -6, -4, -3, 10]) == [
        [-7, -3, 10],
        [-6, -4, 10]
    ]
