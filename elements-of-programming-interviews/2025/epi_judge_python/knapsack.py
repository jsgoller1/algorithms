import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))

"""
Is this like coin change? (i think that's "unbounded" knapsack; this is 0-1 knapsack?)
    - no clocks: you get 0
    - first clock: You can take it if it fits (get its value) or not (get 0)
    - first two clocks: max(take it if it fits, don't take it)
    - first three clocks: max(take it if it fits, don't take it)

2d dp table? cols are clocks, rows are capacity? breaks if capacity is huge

what if like coin change: 
    optimal(clocks, capacity) {
        // Can use indexes instead of array slicing, then we can cache idx, capacity pairs 
        return max(optimal(clocks[1:], capacity), optimal(clocks[1:], capacity-clocks[0]))
    }

do we need to sort by weight first? have the intuition we do but can't explain why; feels necessary for coin change. 
"""


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    if sum([item.weight for item in items]) <= capacity:
        return sum([item.value for item in items])
    dp = [0] * (capacity+1)
    for item in items:
        w, v = item.weight, item.value
        for i in range(capacity, w-1, -1):
            dp[i] = max(dp[i], v + dp[i-w])
    return dp[-1]

@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
