import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

"""
We have 3 possible cases:
- partial overlap 
    - only possible if the sorted heights and lengths are intermixed 
- total overlap / envelopment 
    - only possible when one rectangle is equal or greater in area
- no overlap
    default case

Suppose we reassign so that r1 is the larger of the two rectangles (unless eq),
and we have: 
- verticals: [r1.low, r1.hi, r2.low, r2.hi]
- horizontals: [r1.left, r1.right, r2.left, r2.right],
then we sort verticals and horizontals.
if:
    - either verticals or horizontals are the same as unsorted:
        - no overlap 
    - [r1.lo, r1.hi] is in/eq to [r2.lo, r2.hi] AND [r1.left, r1.right] is in/eq to [r2.left, r2.right]
        - total overlap occurs, return r2
    - otherwise, we have partial overlap:
        - and our overlapping area should be the 2 points in the middle of each array 
"""

# Assume it's bottom left corner 
Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def get_ranges(rect):
    # Assume
    hi = rect.y + rect.height
    lo = rect.y
    left = rect.x
    right = rect.x + rect.width
    return hi, lo, left, right

def create_rectangle(lo, hi, left, right):
    return Rect(left, lo, right-left, hi-lo)


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    hi1, lo1, left1, right1 = get_ranges(r1)
    hi2, lo2, left2, right2 = get_ranges(r2)

    verticals = [lo1, hi1, lo2, hi2] if lo1 < lo2 else [lo2, hi2, lo1, hi1]
    horizontals = [left1, right1, left2, right2] if left1 < left2 else [left2, right2, left1, right1]
    sorted_verticals = sorted(verticals[:])
    sorted_horizontals = sorted(horizontals[:])

    # No overlap. Overlapping occurs when sorting causes both the horizontals and verticals
    # to be interleaved, with an edge case of the leftmost and rightmost are equal (or lowest and highest).
    # If we have the 4 values and they are distinct and remain in the same order, they don't overlap
    verticals_are_sorted = sorted_verticals == verticals
    verticals_are_distinct =  len(sorted_verticals) == len(set(sorted_verticals))
    horizontals_are_sorted = sorted_horizontals == horizontals
    horizontals_are_distinct = len(sorted_horizontals) == len(set(sorted_horizontals))
    if (verticals_are_sorted and verticals_are_distinct) or (horizontals_are_sorted and horizontals_are_distinct):
        return Rect(0, 0, -1, -1)

    # When we overlap, we take the middle horizontals and verticals as the bounds for our rectangle
    return create_rectangle(sorted_verticals[1], sorted_verticals[2], sorted_horizontals[1], sorted_horizontals[2])

for r1, r2, overlap in [
    # No overlap
    [Rect(0, 0, 10, 10), Rect(100, 100, 10, 10), Rect(0, 0, -1, -1)],
    # Corner overlap
    [Rect(0, 0, 10, 10), Rect(-5, -5, 10, 10), Rect(0, 0, 5, 5)],
    # Total envelopment
    [Rect(0, 0, 10, 10), Rect(5, 5, 1, 1), Rect(5, 5, 1, 1)],
    # Border total envelopment
    [Rect(0, 0, 10, 10), Rect(0, 0, 1, 1), Rect(0, 0, 1, 1)],
    # Single point overlap
    [Rect(0, 0, 10, 10), Rect(10, 10, 10, 10), Rect(10, 10, 0, 0)]
]:
    actual = intersect_rectangle(r1,r2)
    assert overlap == actual, f"{r1}, {r2}: {actual} != {overlap}"

def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))