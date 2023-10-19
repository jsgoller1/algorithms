from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ranges = []
        for num in nums:
            if num == lower:
                lower += 1
            elif num == upper:
                ranges.append([lower, upper-1])
                lower = upper + 1
            else:
                ranges.append([lower, num-1])
                lower = num+1

        if not (lower > upper):
            ranges.append([lower, upper])
        return ranges


s = Solution()
cases = [
    # nums, upper, lower
    ([0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]]),
    ([0, 1, 2, 3, 4], 0, 5, [[5, 5]]),
    ([0, 1, 2, 3, 4, 5], 0, 5, []),
    ([], 0, 0, [[0, 0]]),
    ([], 0, 99, [[0, 99]]),
    ([], 1, 1, [[1, 1]]),
    ([-1], -2, -1, [[-2, -2]])

]
for i, case in enumerate(cases):
    nums, lower, upper, expected = case
    actual = s.findMissingRanges(nums, lower, upper)
    assert actual == expected, f"{i}: {nums}, {lower}, {upper}\n{actual} != {expected}"
