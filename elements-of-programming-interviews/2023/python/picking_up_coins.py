import collections
from heapq import heapify, heappush, heappop
from typing import List
from math import ceil

from test_framework import generic_test

"""
caching: (l,r)
base cases: 2: pick larger, 1: pick only option, empty array: return 
regular case:
        best of the following:
            arr[left] + max(best of arr missing second left, best of arr missing right)
            arr[right] + max(best of arr missing left, best of arr missing second right)
"""


def maximum_revenue_greedy(coins):
    # Wrong on ([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])
    # gives 155, not 140
    coins = collections.deque(coins)
    p1, p2 = [], []
    while coins:
        p1.append(coins.popleft() if coins[0] >= coins[-1] else coins.pop())
        if coins:
            p2.append(coins.popleft() if coins[0] >= coins[-1] else coins.pop())
    return sum(p1)


def maximum_revenue_heap(coins):
    # Wrong on ([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])
    # gives 155, not 140
    heap = []
    for coin in coins:
        heappush(heap, -coin)
    total = 0
    half = int(ceil(len(coins)/2))
    for _ in range(half):
        total += (-1 * heappop(heap))
    return total


def maximum_revenue_any_pick(arr: List[int]) -> int:
    # Probably wrong because we look only at the strategies player 2
    # employs that result in maximum revenue for player 1; does not
    # assume player 2 wants to minimize player 1's score.
    # Wrong on ([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])
    # gives 155, not 140

    cache = {}

    def recurse(l, r):
        if l > r:
            return 0
        if (l, r) not in cache:
            left_pick = arr[l] + max(recurse(l+2, r), recurse(l+1, r-1))
            right_pick = arr[r] + max(recurse(l, r-2), recurse(l+1, r-1))
            cache[(l, r)] = max(left_pick, right_pick)
            print(f"{l}:{r} ({cache[(l, r)]}): {arr[l:r+1]}")
        return cache[(l, r)]
    return recurse(0, len(arr)-1)


def maximum_revenue_only_p1(arr: List[int]) -> int:
    # Also wrong. Tries only adding to score if it's player 1's turn, but
    # still picks strategies for player 2 that maximize player 1's score.
    # Wrong on ([25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])
    # gives 155, not 140
    cache = {}

    def recurse(is_player_1, l, r):
        if l > r:
            return 0
        if (l, r) not in cache:
            left_pick = (arr[l] if is_player_1 else 0) + recurse(not is_player_1, l+1, r)
            right_pick = (arr[r] if is_player_1 else 0) + recurse(not is_player_1, l, r-1)
            cache[(l, r)] = max(left_pick, right_pick)
            # print(f"{l}:{r} ({cache[(l, r)]}): {arr[l:r+1]}")
        return cache[(l, r)]
    return recurse(True, 0, len(arr)-1)


def maximum_revenue(arr: List[int]) -> int:
    cache = {}

    def recurse(l, r):
        if l > r:
            return 0
        if (l, r) not in cache:
            left_pick = arr[l] + min(recurse(l+2, r), recurse(l+1, r-1))
            right_pick = arr[r] + min(recurse(l, r-2), recurse(l+1, r-1))
            cache[(l, r)] = max(left_pick, right_pick)
        return cache[(l, r)]
    return recurse(0, len(arr)-1)


if __name__ == '__main__':
    cases = [
        # (2, [1, 2]),
        # (5, [1, 2, 3]),
        # (7, [4, 1, 2, 3]),  # sums to 10
        # (29, [1, 1, 25, 2, 2]),
        # (27, [1, 25, 2, 2]),
        (140, [25, 5, 10, 5, 10, 5, 10, 25, 1, 25, 1, 25, 1, 25, 5, 10])  # sums to 188
    ]

    for expected, coins in cases:
        actual = maximum_revenue(coins)
        assert actual == expected, f"{actual} != {expected} ({coins})"
    exit(
        generic_test.generic_test_main('picking_up_coins.py',
                                       'picking_up_coins.tsv',
                                       maximum_revenue))
