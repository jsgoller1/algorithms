class Solution:
    def findMissingRanges(self, nums, lower: int, higher: int):
        if not nums:
            return [[lower, higher]]
        ranges = []
        for num in nums:
            if lower < num:
                ranges.append([lower, num-1])
            lower = num+1
        if higher > nums[-1]:
            ranges.append([nums[-1]+1, higher])
        return ranges


s = Solution()
for nums, lower, upper, actual in [
    ([1, 3, 5], -10, 10, [[-10, 0], [2, 2], [4, 4], [6, 10]]),
    ([0, 1, 3, 50, 75], 0, 99, [[2, 2], [4, 49], [51, 74], [76, 99]]),
    ([-1], -1, -1, []),
    ([1, 2, 3, 4, 5], 1, 5, []),
    ([], 1, 5, [[1, 5]])
]:
    expected = s.findMissingRanges(nums, lower, upper)
    assert actual == expected, f"{nums}, {lower}, {upper}: {actual} != {expected}"
