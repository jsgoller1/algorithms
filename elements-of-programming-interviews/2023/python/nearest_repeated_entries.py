from typing import List

from test_framework import generic_test

"""
in: list of strs
out: int, distance between closest two repetitions 

edges:
    - empty list
    - no repetitions (what do we return? -1?)
    - all repetitions
    - all equal distance 

O(n) space, time:
    - hash every word to index each time it appears
    - hash every word to distance since last occured (inf if first occurence)
        - don't need this, just best
    - return min distance 

Can't do better than O(n) time, need to examine each word
Do better than O(n) space? Need to keep track of each word.
"""
import math


def find_nearest_repetition(paragraph: List[str]) -> int:
    best = float('inf')
    last_idx = {}
    for i, word in enumerate(paragraph):
        if word in last_idx:
            best = min(i-last_idx[word], best)
        last_idx[word] = i
    return best if not math.isclose(best, float('inf')) else -1


if __name__ == '__main__':
    """
    cases = [
        ([], -1),
        (["no", "a", "b"], -1),
        (["no", "a", "b", "no"], 2),
        (["no", "no", "b", "no"], 0)
    ]
    for arg, expected in cases:
        actual = find_nearest_repetition(arg)
    assert actual == expected, f"{actual} != {expected}"
    """
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
