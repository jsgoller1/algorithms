from typing import List

# def find(val, uf):
#    if uf[val] == val:
#        return val
#    uf[val] = find(uf[val], uf)
#    return uf[val]

# def union(uf, a, b):
#    rootA = find(a, uf)
#    rootB = find(b, uf)
#    if rootA != rootB:
#        uf[rootA] = rootB


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        paths = {}
        best = 0

        for num in nums:
            if num-1 not in nums:
                curr = num
                path_len = 1
                while curr+1 in nums:
                    curr += 1
                    path_len += 1
                best = max(best, path_len)
        return best


# [-8, -4, -3, -2, -1, 0, 2, 4, 5, 6, 7]
s = Solution()
cases = [
    ([4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3], 5),
    ([0, -1], 2),
    ([], 0),
    ([1], 1),
    ([1, 2, 3, 4], 4),
    ([4, 3, 2, 1], 4),
    ([1, 3, 5, 7], 1),
    ([1, 2, 2, 3], 3),
]
for i, case in enumerate(cases):
    nums, expected = case
    actual = s.longestConsecutive(nums)
    assert actual == expected, f"{i}, {nums}: {actual} != {expected}"
