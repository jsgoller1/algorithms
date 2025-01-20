import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

Interval = collections.namedtuple('Interval', ('left', 'right'))


def overlap(int_a, int_b):
    lesser, greater = (int_a, int_b) if int_a.left <= int_b.left else (int_b, int_a)
    return not (lesser.left <= lesser.right < greater.left <= greater.right)

def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:
    merged = []
    for interval in disjoint_intervals:
        if not overlap(interval, new_interval):
            merged.append(interval)
        else: 
            new_interval = Interval(left=min(interval[0], new_interval[0]), right=max(interval[1], new_interval[1]))
    return [interval for interval in sorted(merged + [new_interval])]


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('interval_add.py',
                                       'interval_add.tsv',
                                       add_interval_wrapper,
                                       res_printer=res_printer))
