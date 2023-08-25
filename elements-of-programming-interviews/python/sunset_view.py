from typing import Iterator, List

from test_framework import generic_test

"""
- Input is a list of height
- Output is list of indices

[6,5,4,3,2,1]
[1,2,3,4]
"""


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []
    for i, height in enumerate(sequence):
        while stack and stack[-1][1] <= height:
            stack.pop()
        stack.append((i, height))
    return [item[0] for item in reversed(stack)]


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
