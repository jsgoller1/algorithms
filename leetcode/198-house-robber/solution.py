"""
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night. Given a list of non-negative integers
representing the amount of money of each house, determine the maximum amount
of money you can rob tonight without alerting the police.

Example 1:
Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
------------------------------------------------------------------------------
- We did this problem for Bradfield during the DP section, but I struggled a lot with it at
the time, so resolving it will be good practice.

- Is there a recurrence relation here? Let's see if working upwards reveals one:
  - If we have two houses, rob the bigger one
  - If we have three houses, rob either the middle, or the
    edge houses.
  - If we have four houses, we take either the selection from 3 or the new edge + the one from 2.
  - If we have 5, we either take the 4 with no addition, or the 3 with a new addition
- So it looks like the recurrence is:
  - rob(n) = max(rob(n-1), rob(n-2) + new edge house)
  - Let's try it with example 2:
    - [2,7] = rob 7 (base case)
    - [2,7,9] = rob 2 and 9 (base case)
    - [2,7,9,3] = rob n = 3 (11) > rob n = 2 + house 3 (10)
    - [2,7,9,3,1] = rob(n = 4) < rob (n = 3) + house 4 (12)

- We can use a bottom-up approach with a for loop to complete this in n time,
  or a simple tail recursion

- Solution works for 49 cases, but breaks on TLE, so we should implement caching
and switch to an approach that uses indices instead of arrays to avoid copying
"""


class Solution:
    def rob(self, nums):
        return self._rob(nums, {})

    def _rob(self, nums, cache):
        key = tuple(nums)
        if key in cache:
            return cache[key]
        if not nums:
            cache[key] = 0
        elif len(nums) in [1, 2]:
            cache[key] = max(nums)
        else:
            cache[key] = max(self._rob(nums[1:], cache),
                             nums[0] + self._rob(nums[2:], cache))
        return cache[key]


if __name__ == '__main__':
    s = Solution()
    assert s.rob([1, 2, 3, 1]) == 4
    assert s.rob([2, 7, 9, 3, 1]) == 12
