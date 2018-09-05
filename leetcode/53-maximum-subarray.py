"""
https://leetcode.com/problems/maximum-subarray/description/

I solved this as part of my Bradfield Algorithms class; all of my SUPER heuristic
occurred over Slack with @robot-dreams.
"""


class Solution:
    def maxSubArray(self, nums):
        """
        Get the maximum sum possibly by any
        subarray of nums.

        :type nums: List[int]
        :rtype: int
        """
        self.cache = {}
        self.arr = nums
        for i in range(len(nums)):
            self.cache[i] = self.max_subarray_sum(i)
        print(self.cache)
        return self.cache[max(self.cache, key=self.cache.get)]

    def max_subarray_sum(self, i):
        """
        Get the max sum for a subarray of arr
        ending at and including index i.

        :type nums: List[int]
        :type i: int
        :rtype: int
        """
        if i in self.cache:
            return self.cache[i]
        if i == 0:
            return self.arr[0]
        else:
            return max(self.max_subarray_sum(i-1) + self.arr[i], self.arr[i])


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
