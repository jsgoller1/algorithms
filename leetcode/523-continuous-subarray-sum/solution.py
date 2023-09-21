from typing import List

# k = rsum - rsum_prev
# k + rsum_prev = rsum
# rsum_prev = rsum - k

# entire array sums to multiple of k
# current prefix - prev prefix is multiple of k


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False

        if k == 1:
            return True

        prefixes = {}
        rsum = 0
        for i, val in enumerate(nums):
            rsum += val
            if (rsum % k in prefixes and prefixes[rsum % k]+1 < i) or (i != 0 and rsum % k == 0):
                print(f"prefixes: {prefixes}, i: {i}, rsum: {rsum}")
                return True
            if (rsum % k not in prefixes):
                prefixes[rsum % k] = i

        return False


s = Solution()
cases = [
    # ([5, 2, 4], 5, False),
    ([5, 0, 0, 0], 3, True),
    ([0, 1], 2, False),
    ([], 5, False),
    ([5], 5, False),
    ([5, 5], 5, True),
    ([2, 3, 4, 5, 0, 1], 1, True),
    ([2, 3, 4, 5, 1], 1, True),
    ([23, 2, 6, 4, 7], 13, False),
    ([7, 13, 25, 37, 44], 6, True),
    ([23, 2, 6, 4, 7], 6, True),
    ([23, 2, 4, 6, 7], 6, True),
    ([0, 0], 1, True),
]
for arr, k, expected in cases:
    actual = s.checkSubarraySum(arr, k)
    assert actual == expected, f"{arr}, {k}: {actual} != {expected}"
    print("---")
