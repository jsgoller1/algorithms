"""
Statement

Suppose we have a list of points in the plane. If we were
to draw an isoceles triangle where the two equal sides were drawn
along the x and y axes, what is the minimum length that the third
side would need to be to cover all of the points (they are covered
if they are inside the triangle or on the edge)?

Input:
first line - int count between 1 and 10**5
following lines - x/y pairs

Output:
minimum length of the two equal sides

Notes:
- We only need to care about the "most extreme" points;
if we cover the highest x and highest y points, we will cover the rest

- how do we tell if a point is inside the triangle?
  - there is a ratio of "how high it may be given how far to the right it is" and vice versa
  - that ratio is determined by the slope of line between the two points

-----------
Understand / Plan
"""

import sys

if __name__ == '__main__':
    throwaway = int(input())  # don't need count
    max_side_size = 0
    for point_line in sys.stdin:
        x, y = point_line.split()
        x = int(x)
        y = int(y)
        if x + y > max_side_size:
            max_side_size = x+y
    print(max_side_size)
