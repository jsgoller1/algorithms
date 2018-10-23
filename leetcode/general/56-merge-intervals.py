"""
Given a collection of intervals, merge all overlapping ones.

Some overlap:
In: [[1,3], [2,6], [8,10], [15,18]]
Out: [[1,6], [8,10], [15,18]]

Some overlap:
In: [[1,], [9,16], [8,10], [8,18]]
Out: [[1,6], [8,10], [15,18]]

Edge overlap:
In: [[1,4],[4,5]]
Out: [[1,5]]

No overlap:
In: [[1,5], [6,10]]
Out: [[1,5], [6,10]]

All overlap:
In: [[1,5], [4,11], [8,15]]
Out: [[1,15]]

Constraints:
  - Lists of integers
----------------------------------------
Cases:
  - Empty list
    - Return input
  - Single interval
    - Return input
  - Multiple intervals
    - No overlap
      - Return input
    - Some overlap
      - Return less intervals
    - All overlap
      - Return a single interval

- Sort list
- Iterate through list two intervals at a time. If the lower
bound of the second interval falls within the bounds of the first
interval, merge them.
"""


def intervalKey(interval):
    return interval.start


class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals, key=intervalKey)
        i = 0
        while(i < len(intervals)-1):
            low = intervals[i]
            high = intervals[i + 1]
            if high.start <= low.end <= high.end or low.start <= high.end <= low.end:
                newInterval = Interval(
                    min(low.start, high.start), max(low.end, high.end))
                intervals[i] = newInterval
                intervals.remove(intervals[i + 1])
            else:
                i += 1
        return intervals


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


if __name__ == '__main__':
    s = Solution()
    # [[1, 6], [8, 10], [15, 18]]
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    typedIntervals = [Interval(each[0], each[1]) for each in intervals]
    print(s.mergeIntervals(typedIntervals))

    intervals = [[[1, 4], [2, 3]]]
    typedIntervals = [Interval(each[0], each[1]) for each in intervals]
    print(s.mergeIntervals(typedIntervals))

    # [[1, 5]]
    #print(s.mergeIntervals([[1, 4], [4, 5]]))

    # Out: [[1, 5], [6, 10]]
    #print(s.mergeIntervals([[1, 5], [6, 10]]))

    # Out: [[1, 15]]
    #print(s.mergeIntervals([[1, 5], [4, 11], [8, 15]]))
