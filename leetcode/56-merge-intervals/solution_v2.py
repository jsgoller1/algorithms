"""
In: list of lists of intervals (always 2 bounds)
Out: merged list of intervals covering input list with no overlaps

- Could be up to 10^4 (10000) intervals in list; each interval could be
between 0 and 10,000.
- Do we have constraints on memory / running time?
    - Not given
----------------------------------------
Cases:
    - Some intervals overlap, some don't
        - [1,3], [2,4], [6,8] -> [1,4], [6,8]
    - All overlap
        - [1,10], [2,3], [4,5] -> [1,10]
    - No overlap
        - [1,2], [3,4] -> same
    - Duplicate intervals
        - [1,2], [1,2], [3,4] -> [1,2], [3,4]
    - Only one interval
        - [1,10] -> same
    - Can also be combinations of cases above (e.g. duplicates + all overlap)

Possible approaches:
    - Worst / brute force: compare every pair of intervals; O(n^2)
        - Worst input will be 10,000 non-overlapping 
    - We can sort the intervals first; this will eliminate needing to test intervals with non-neighbors
        - sorting is O(nlogn)
    - After sorting, we can neighbor-test:
        - take first two; if they overlap, merge them. If not, move on to the next two. Repeat until
        there are two or fewer, or we reach the end of the list. O(n) (superseded by nlogn for sort)
        - Exit cond: two or fewer non-overlapping, or final two in input and no overlap
--------

def merge_intervals(interval_1, interval_2):
    all_bounds = set(interval_1) | set(interval_2)
    return [min(all_bounds), max(all_bounds)] 

# Make sure to use type sigs
def should_merge(interval_1, interval_2):
    return (interval_1[0] <= interval_2[0] <= interval_1[1]) or (interval_2[0] <= interval_1[0] <= interval_2[1])

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    first, second = 0, 1
    merged = []
    while second < len(intervals):
        if should_merge(intervals[first], intervals[second]):
            merged.append(merge_interval(intervals[first], intervals[second]))
        else:
            first +=1
            second +=1
    return merged
"""
from typing import List

def merge_intervals(interval_1: List[int], interval_2: List[int]) -> (int,int):
    return min(interval_1[0], interval_2[0]), max(interval_1[1], interval_2[1]) 

# Make sure to use type sigs
# Should be part of Solution cls?
def should_merge(interval_1: List[int], interval_2: List[int]) -> bool:
    return (interval_1[0] <= interval_2[0] <= interval_1[1]) or (interval_2[0] <= interval_1[0] <= interval_2[1])

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        first, second = 0, 1
        intervals = sorted(intervals)
        while second < len(intervals):
            if should_merge(intervals[first], intervals[second]):
                low, hi = merge_intervals(intervals[first], intervals[second])
                intervals[first][0] = low 
                intervals[first][1] = hi 
                intervals.pop(second)
            else:
                first +=1
                second +=1
        return intervals

s = Solution()
test_cases = [
    (
        "Given case 1",
        [[1,3],[2,6],[8,10],[15,18]], 
        [[1,6],[8,10],[15,18]]
    ),
    (
        "Given case 2",
        [[1,4],[4,5]], 
        [[1,5]]
    ),
    (
        "No overlap",
        [[1,2], [3,4]], 
        [[1,2], [3,4]]
    ),
    (
        "Duplicate intervals",
        [[1,2], [1,2], [3,4]],
        [[1,2], [3,4]]
    ),
    (
        "Only one interval",
        [[1,10]], 
        [[1,10]]
    )
]
for name, in_val, out_val in test_cases:
    actual = s.merge(in_val)
    assert  actual == out_val, f"Failed {name}: {actual}"
