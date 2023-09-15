from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def is_peak(m: int):
            if len(nums) == 1:
                return True
            if m == 0:
                return nums[m] > nums[m+1]
            elif m == len(nums)-1:
                return nums[m-1] < nums[m]
            else:
                return nums[m-1] < nums[m] > nums[m+1]

        l, r = 0, len(nums)-1
        while l <= r:
            m = (l + r) // 2
            # print(l, m, r)
            if is_peak(m):
                return m
            elif nums[m] < nums[m+1]:
                l = m+1
            else:  # nums[m-1] < nums[m]
                r = m-1
        return l


s = Solution()
cases = [
    ([0], 0),
    ([0, 1], 1),
    ([0, 1, 0], 1),
    ([0, 1, 2], 2),
    ([3, 1, 0], 0),
    ([1, 2, 3, 1], 2)
]
for nums, expected in cases:
    actual = s.findPeakElement(nums)
    assert actual == expected, f"{nums}: {actual} != {expected}"
