"""
Given an array with n objects colored red, white or blue, sort them
in-place so that objects of the same color are adjacent, with the
colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
- A rather straight forward solution is a two-pass algorithm using counting sort. First, iterate the array counting number of 0's, 1's, and 2's,
 then overwrite array with total number of 0's, then 1's and followed by 2's.
- Could you come up with a one-pass algorithm using only constant space?
---------------------------------------------------------------------------
In: list[int]
Out: Nothing, sort in place

- Brute force approach would be to write mergesort
- I don't know what "counting sort" means
- For a two-pass, in place approach:
  - set zeroes, ones, twos to zero
  - count each color, incrementing respective variable
  - overwrite array with colors in sorted order depending on count

- for one pass, do something like dutch national flag sort:
  - set two pivots
  - set zeroes, ones, twos to zero
  - for each item in the array, starting
"""

import collections


class Solution:
    def sortColors(self, nums):
        counts = collections.Counter(nums)
        i = 0
        colors = [0, 1, 2]
        for color in colors:
            while counts[color]:
                nums[i] = color
                i += 1
                counts[color] -= 1
        return


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2])
    ]
    for case in cases:
        s.sortColors(case[0])
        assert case[0] == case[1]
