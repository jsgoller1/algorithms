"""
Given a non-empty array of integers, every element appears twice
except for one. Find that single one. Note: Your algorithm should
have a linear runtime complexity. Could you implement it without
using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Example 3:
Input: [1,1,2,5,2,3,3]
Output: 5
------------------------------------------------------
In: List[int]
Out: int
- Can we safely assume that all arrays are non-empty?

- We can use the normal duplicate-finding approach with
a dict if we were to use O(N) memory
- We could try an approach where we "do and undo"; each time
we see a number for the first time, add it, then take it away.
  - How do we know if we've seen a number before?
  - What operation is "second iteration undoes the first"?
    - Flipping a sign
- Could we use two pointers?
"""


class Solution(object):
    def singleNumberLinear(self, nums):
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        return seen.pop()

    def singleNumber(self, nums):
        ans = 0
        for num in nums:
            ans ^= num
        return ans


if __name__ == '__main__':
    s = Solution()
    assert s.singleNumber([1, 1, 2, 3, 3, 4, 4]) == 2
