import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def left(rect):
    return rect.x


def right(rect):
    return rect.x + rect.width


def down(rect):
    return rect.y


def up(rect):
    return rect.y + rect.height


def interval_overlap(x, l, r):
    return l <= x <= r


def line_overlap(a1, a2, b1, b2):
    return interval_overlap(a1, b1, b2) or \
        interval_overlap(a2, b1, b2) or \
        interval_overlap(b1, a1, a2) or \
        interval_overlap(b2, a1, a2)


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    if not (line_overlap(left(r1), right(r1), left(r2), right(r2)) and
            line_overlap(down(r1), up(r1), down(r2), up(r2))):
        return Rect(0, 0, -1, -1)

    x_vals = sorted([left(r1), right(r1), left(r2), right(r2)])
    y_vals = sorted([up(r1), down(r1), up(r2), down(r2)])
    return Rect(x_vals[1], y_vals[1], x_vals[2] - x_vals[1], y_vals[2] - y_vals[1])


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
    """
    r1 = Rect(76, 9, 12, 14)
    r2 = Rect(20, 1, 62, 60)
    # print(interval_overlap(up(r1), down(r2), up(r2)))
    """
    exit(
        generic_test.generic_test_main('rectangle_intersection.py',
                                       'rectangle_intersection.tsv',
                                       intersect_rectangle_wrapper,
                                       res_printer=res_printer))
