"""
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system 
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight 
without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
    0 <= nums.length <= 100 (Up to 100 houses, possibly none)
    0 <= nums[i] <= 400 (Each house has 0 to 400 moneys)

Edge cases:
    - 0 houses
    - houses arranged a,b,c where b > a,c but a+c > b (not sure if edge case)
-------------------------------
Brute force:
    Try every possible robbing (bad performance, not going to waste time analyzing it)

Does adding more houses change anything? Can we re-use knowledge
1 - rob it
[10]

2 - rob greater of the two
[10, 11]

3 - rob middle if greater than sum of edges
[10,11,12] (rob edges)
[10,11, 0] (rob middle)

4 - How can we reuse knowledge about 3? 
At each step i, we have the following options, and should pick the best:
    1: Rob i and i-2, but not i-1
    2: Only rob i-2

[10,11,12,13,14]
For [10,...,14], we know:
    - optimal is rob 14, 12, 10 (36).
    - What do we need to know to correctly handle adding 15? 2?
        - 15: what would have been the result of not robbing 14, but robbing 13 instead? 
        -  
--------------
best_if_robbed = 0
best_if_skipped = 0
for each house in arr:
    best_if_robbed, best_if_skipped = best_if_skipped + house, best_if_robbed
return max(best_if_robbed, best_if_skipped)
"""
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_rob = prev_skip = skip = 0
        for house in nums:
            skip = max(prev_rob, prev_skip)
            prev_rob, prev_skip = prev_skip + house, skip
        return max(prev_rob, prev_skip)


s = Solution()
cases = [
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12),
    ([0, 0, 0, 15], 15),
    ([15, 0, 0, 15], 30)
]
for houses, expected in cases:
    actual = s.rob(houses)
    assert actual == expected, f"{houses}, {expected} != {actual}"
