import collections
import functools
from typing import List, Set

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

Subarray = collections.namedtuple('Subarray', ('start', 'end'))

"""
["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"]
       |    |    |              |         |              |     |
       1    2    1              2         3              1     3 

   1 ... 2 ...3 ... 1,2,3 ... 3 ... 2 ... 1

"""

# b...... b c e ......... b
# first remove l/r characters that aren't in keywords

# No keywords, no paragraph, no keywords in paragraph?
# assume for now none of these can happen


def find_smallest_subarray_covering_set_attempt_one(paragraph: List[str],
                                                    keywords: Set[str]) -> Subarray:
    subarr = collections.deque([])
    current_kwords = collections.Counter()
    left, right = 0, len(paragraph)-1
    for i, word in enumerate(paragraph):
        if word in keywords:
            current_kwords[word] += 1
            subarr.append(i)
        while subarr and current_kwords[paragraph[subarr[0]]] > 1:
            current_kwords[paragraph[subarr[0]]] -= 1
            subarr.popleft()
        if len(current_kwords) == len(keywords) and ((subarr[-1] - subarr[0]) <= (right-left)):
            left, right = subarr[0], subarr[-1]
    return Subarray(left, right)


def find_smallest_subarray_covering_set(paragraph: List[str],
                                        keywords: Set[str]) -> Subarray:
    counts = collections.Counter()
    best = Subarray(0, len(paragraph)-1)
    left = 0
    for right, word in enumerate(paragraph):
        if word not in keywords:
            continue
        counts[word] += 1

        while left < len(paragraph) and not (counts[paragraph[left]] == 1):
            if paragraph[left] in counts:
                counts[paragraph[left]] -= 1
            left += 1

        if len(counts) == len(keywords) and ((right - left) <= (best.end - best.start)):
            best = Subarray(left, right)
    return best


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
    """
    cases = [
        (["a", "b", "c", "b", "a", "d", "c", "a", "e", "a", "a", "b", "e"], set(["b", "c", "e"]), Subarray(6, 11)),
        (["a", "b", "c", "e", "a"], set(["b", "c", "e"]), Subarray(1, 3)),
        (["a", "b", "c", "e", "a", "e"], set(["b", "c", "e"]), Subarray(1, 3)),
        (["b", "a", "b", "c", "e", "a", "e"], set(["b", "c", "e"]), Subarray(2, 4)),
        (["b", "a", "c", "c", "c", "b", "c", "e", "a", "e"], set(["b", "c", "e"]), Subarray(5, 7))

    ]
    for paragraph, keywords, expected in cases:
        actual = find_smallest_subarray_covering_set(paragraph, keywords)
        assert expected == actual, f"\nparagraph: {paragraph}\nkeywords: {keywords}\n{expected} != {actual}"
    """
    exit(
        generic_test.generic_test_main(
            'smallest_subarray_covering_set.py',
            'smallest_subarray_covering_set.tsv',
            find_smallest_subarray_covering_set_wrapper))
