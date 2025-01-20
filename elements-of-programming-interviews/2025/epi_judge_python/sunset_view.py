from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: Iterator[int]) -> List[int]:
    stack = []
    for i, height in enumerate(sequence):
        while stack and stack[-1][1] <= height:
            stack.pop()
        stack.append((i, height))
    return [idx for idx,height in stack[::-1]] if stack else []


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
