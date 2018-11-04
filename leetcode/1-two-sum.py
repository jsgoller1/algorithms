"""
Given an array of integers, return indices of the
two numbers such that they add up to a specific target.

You may assume that each input would have exactly
one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,

return [0, 1].
--------------------------------------
- Had notes but deleted old file

- Created sorted version of original
- use high/low pointer in sorted array, decrement or increment til solution is found
- Return array of indices in original array, be sure to catch case like [3,3]
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        O(n) solution: For each
        number in the array, map
        its complement to its index.
        If we find a value that is the
        complement of some other value,
        return the indices of both.
        (this beat 99.74% of existing solutions)
        """
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target - nums[i]] = i
            else:
                return [map[nums[i]], i]
        return [-1, -1]

    def twoSumLinearithmic(self, nums, target):
        """
        O(nlogn) - sort the array, then maintain
        high and low pointers in it. If arr[hi] + arr[low]
        is greater than the target, decrement hi. If lower,
        increment low. Once the two items are found,
        find their original indices and return them.
        """
        # Create sorted arr
        sortedArr = sorted(nums)
        hi = len(sortedArr) - 1
        lo = 0

        # Get indicies in sorted arr
        while sortedArr[lo] + sortedArr[hi] != target:
            if sortedArr[lo] + sortedArr[hi] > target:
                hi -= 1
            else:
                lo += 1

        # Convert to indices in unsorted arr
        solution = []
        for i in range(len(nums)):
            if nums[i] == sortedArr[lo]:
                solution.append(i)
                break

        for i in range(len(nums)-1, -1, -1):
            if nums[i] == sortedArr[hi]:
                solution.append(i)
                break

        return solution


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([3, 3], 6) == [0, 1]
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
