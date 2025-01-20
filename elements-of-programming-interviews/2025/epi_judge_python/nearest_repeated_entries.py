from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    best = float('inf')
    seen = {}
    for i, word in enumerate(paragraph):
        if word in seen:  
            seen_idx = seen[word]
            best = min(best, i - seen_idx)
        seen[word] = i 
    return -1 if best == float('inf') else best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
