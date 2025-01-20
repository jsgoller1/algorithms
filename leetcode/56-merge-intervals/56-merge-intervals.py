def is_overlapping(interval_a, interval_b):
    return not (interval_a[0] <= interval_a[1] < interval_b[0] <= interval_b[1])


def merge_intervals(interval_a, interval_b):
    bounds = interval_a + interval_b
    bounds.sort()
    return [bounds[0], bounds[-1]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        intervals.sort()
        i, j = 0, 1
        while j < len(intervals):
            if is_overlapping(intervals[i], intervals[j]):
                intervals[i] = merge_intervals(intervals[i], intervals[j])
                del intervals[j]
            else:
                i += 1
                j += 1
        return intervals
