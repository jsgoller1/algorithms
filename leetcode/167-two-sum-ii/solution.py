from bisect import bisect_left
from typing import List


class Solution:
    def twoSumLinearithmic(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):
            comp = target-val
            j = bisect_left(numbers, target-val)
            if j != len(numbers) and numbers[j] == comp and j != i:
                return sorted([i+1, j+1])

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        total = numbers[l] + numbers[r]
        while total != target:
            if total < target:
                l += 1
            else:
                r -= 1
            total = numbers[l] + numbers[r]
        return [l+1, r+1]


if __name__ == '__main__':
    cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([1, 2, 3], 4, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2])
    ]
    s = Solution()
    for arr, k, expected in cases:
        actual = s.twoSum(arr, k)
        assert actual == expected, f"{arr}, {k}: {actual} != {expected}"
