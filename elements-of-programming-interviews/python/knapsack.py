import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    best_val = [[0 for _ in range(capacity+1)] for _ in range(len(items)+1)]
    for i, item in enumerate(items):
        curr_i = i+1
        for curr_cap in range(capacity+1):
            best_val[curr_i][curr_cap] = best_val[curr_i - 1][curr_cap]
            if curr_cap >= item.weight:
                best_val[curr_i][curr_cap] = max(best_val[curr_i][curr_cap], best_val[curr_i-1][curr_cap - item.weight] + item.value)
    return best_val[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
