import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)


def eliminate_duplicate_linear_space(A: List[Name]) -> None:
    names = set()
    out = []
    for name in A:
        if name.first_name not in names:
            names.add(name.first_name)
            out.append(name.first_name)
    return out 

def eliminate_duplicate(A: List[Name]) -> None:
    A.sort()
    out = []
    i = 0 
    while i < len(A):
        if not out or A[i].first_name != out[-1]:
            out.append(A[i].first_name)
        i += 1
    return out 

@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]
    return executor.run(functools.partial(eliminate_duplicate, names))


def comp(expected, result):
    return all([
        e == r for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
