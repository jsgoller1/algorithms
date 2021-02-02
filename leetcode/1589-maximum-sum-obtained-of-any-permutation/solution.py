from collections import Counter
from typing import List


def interval_sweep_shitty(requests):
    """
    Given a list of ranges, return an array
    where arr[i] equals the number of ranges
    including i.
    """
    bounds_counts = Counter()
    first, last = float('inf'), -float('inf')
    for start, end in requests:
        bounds_counts[start] += 1
        bounds_counts[end+1] -= 1
        first = min(start, end, first)
        last = max(start, end, last)

    frequency = 0
    overlap_count = []
    for val in range(first, last+1):
        frequency += bounds_counts[val]
        overlap_count.append(frequency)
    return overlap_count


def interval_sweep(nums_len, requests):
    """
    Same as above, but borrowing from @lee215's
    technique which is faster.
    """
    counts = [0] * (nums_len+1)
    for start, end in requests:
        counts[start] += 1
        counts[end+1] -= 1

    for i in range(1, nums_len+1):
        counts[i] += counts[i-1]
    return counts


class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse=True)
        overlap_count = interval_sweep(len(nums), requests)
        max_sum = 0
        for i, frequency in enumerate(sorted(overlap_count[:-1], reverse=True)):
            max_sum += frequency*nums[i]
        return max_sum % (10**9 + 7)


s = Solution()
cases = [
    ([1, 2, 3, 4, 5], [[1, 3], [0, 1]], 19),
    ([1, 2, 3, 4, 5, 6], [[0, 1]], 11),
    ([1, 2, 3, 4, 5, 10], [[0, 2], [1, 3], [1, 1]], 47)
]
for nums, requests, expected in cases:
    actual = s.maxSumRangeQuery(nums, requests)
    assert actual == expected, f"{nums, requests}: {expected} != {actual}"
