import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    required = collections.Counter(keywords)
    present = collections.Counter() 
    best_l, best_r = 0, len(paragraph)
    l = r = 0
    while r < len(paragraph):
        r_word = paragraph[r]
        if r_word in required:
            present[r_word] += 1 
            
        if not len(required - present):
            while (paragraph[l] not in required) or (present[paragraph[l]] > 1):
                if paragraph[l] in required:
                    present[paragraph[l]] -= 1
                l += 1 
            best_l, best_r = (l, r) if (r - l < best_r - best_l) else (best_l, best_r)

        r += 1
    return Subarray(best_l, best_r)

"""
p =  ["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]
k = ["b", "c", "e"]
print(find_smallest_subarray_covering_set(p, k))

"""

@enable_executor_hook
def find_smallest_subarray_covering_set_wrapper(executor, paragraph, keywords):
    copy = keywords

    (start, end) = executor.run(
        functools.partial(find_smallest_subarray_covering_set, paragraph,
                          keywords))

    if (start < 0 or start >= len(paragraph) or end < 0
            or end >= len(paragraph) or start > end):
        raise TestFailure('Index out of range')

    for i in range(start, end + 1):
        copy.discard(paragraph[i])

    if copy:
        raise TestFailure('Not all keywords are in the range')

    return end - start + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
