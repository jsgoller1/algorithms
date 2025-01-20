from typing import List

from test_framework import generic_test, test_utils

"""
In: list of strings; strings fit in mem
Out: list of list of strings, grouped by anagrams, must have at least 2

edges:
- empty list, no anagrams, all anagrams

- sort lowercased strings, use as keys 
"""

import collections


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    dd = collections.defaultdict(list)
    for word in dictionary:
        dd["".join(sorted(word.lower()))].append(word)
    return [v for v in dd.values() if len(v) > 1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
