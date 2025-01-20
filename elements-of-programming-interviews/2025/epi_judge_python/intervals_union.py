import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))

Interval = collections.namedtuple('Interval', ('left', 'right'))

"""
Normal union merge algorithm; if a closed and open endpoint fall on the same 
end, closed wins.
"""

# print([(interval.left.val, interval.right.val) for interval in intervals])

def overlap(interval1, interval2):
    # Interval1 is the leftmost 
    interval1, interval2 = (interval1, interval2) if interval1.left.val < interval2.left.val else (interval2, interval1)
    strict_overlap =  interval2.left.val < interval1.right.val
    boundary_overlap = interval1.right.val == interval2.left.val and (interval1.right.is_closed or interval2.left.is_closed)
    return strict_overlap or boundary_overlap

def merge(interval1, interval2):
    if interval1.left.val == interval2.left.val:
        left_end = Endpoint(is_closed=(interval1.left.is_closed or interval2.left.is_closed), val=interval1.left.val)
    else: 
        left_end = interval1.left if interval1.left.val < interval2.left.val else interval2.left  

    if interval1.right.val == interval2.right.val:
        right_end = Endpoint(is_closed=(interval1.right.is_closed or interval2.right.is_closed), val=interval1.right.val)
    else: 
        right_end = interval1.right if interval1.right.val > interval2.right.val else interval2.right   

    return Interval(left_end, right_end)

def union_of_intervals(intervals: List[Interval]) -> List[Interval]:
    intervals.sort(reverse=True, key=lambda interval: interval.left.val)
    output = []
    while intervals: 
        curr = intervals.pop()
        if not (output and overlap(curr, output[-1])):
            output.append(curr)
        else:
            output[-1] = merge(curr, output[-1])
    return output 

@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intervals_union.py',
                                       'intervals_union.tsv',
                                       union_of_intervals_wrapper))
