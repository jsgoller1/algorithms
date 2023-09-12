from typing import List


def envelopes(interval1, interval2):
    return interval1[0] <= interval2[0] <= interval2[1] <= interval1[1]


def overlaps(interval1, interval2):
    return (interval1[0] <= interval2[0] <= interval1[1])


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals = sorted(intervals, key=(lambda interval: interval[0]))
        i = 0
        while i < len(intervals)-1:
            interval1, interval2 = intervals[i], intervals[i+1]
            if envelopes(interval1, interval2):
                del intervals[i+1]
            elif overlaps(interval1, interval2):
                intervals[i] = [interval1[0], interval2[1]]
                del intervals[i+1]
            else:
                i += 1
        return intervals


cases = [
    (
        [[1, 4], [2, 5]],
        [[1, 5]]
    ),
    (
        [[1, 5], [2, 3]],
        [[1, 5]]
    ),
    (
        [[1, 4], [2, 5], [1, 7]],
        [[1, 7]]
    ),
    (
        [[1, 4], [2, 5], [1, 7], [2, 9], [66, 67]],
        [[1, 9], [66, 67]]
    ),
]
s = Solution()
for intervals, expected in cases:
    actual = s.merge(intervals)
    assert actual == expected, f"{intervals}: {actual} != {expected}"
