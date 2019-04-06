"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
-------------------
Input: List[ints]
Output: [List[List[ints]]]

Edge cases:
  - Null / singleton: empty list or one-entry list
  - List will be distinct, no duplicates possible

- The powerset tests if an item is included, so it's a binary value
- We can represent the entire set as a string of n bits; the ith item is 1 if it is in the set
and zero if not.
- The power set is every binstring of length n; loop through all of them, and insert them into a set
so no duplicates occur
- This will get VERY slow for large sets as it's O(2^n)
"""


class Solution(object):
    def subsets(self, nums):
        solution = []
        powersetSize = int("0"+("1" * len(nums)), 2)
        formatStr = '0' + str(len(nums)) + 'b'
        for subsetVal in range(powersetSize+1):
            subsetStr = format(subsetVal, formatStr)
            subset = []
            for i, bit in enumerate(subsetStr):
                if bit == '1':
                    subset.append(nums[i])
            solution.append(subset)
        return solution


if __name__ == '__main__':
    s = Solution()
    tests = [
        ([1, 2, 3], [
            [3],
            [1],
            [2],
            [1, 2, 3],
            [1, 3],
            [2, 3],
            [1, 2],
            []
        ]),
        ([], [[]]),
        ([1], [[], [1]])
    ]

    for test in tests:
        actual = s.subsets(test[0])
        expected = test[1]
        for each in actual:
            assert each in expected
        for each in expected:
            assert each in actual
