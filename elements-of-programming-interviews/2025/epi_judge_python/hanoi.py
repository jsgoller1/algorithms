import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

NUM_PEGS = 3


"""
base cases: 
    n = 1: (0,1)
    n = 2: (0,2), (0,1), (2,1)
recursive case:
    do for n-1, then move the nth ring to the peg we didn't put the n-1 on. Then move the n-1 to it. 
        - n=3: do the n=2 case to move the 1,2 rings to space 1. then move the 3 to peg 2. then move 1,2 to peg 2. 
"""

def compute_tower_hanoi(num_rings: int) -> List[List[int]]:
    def recurse(n, src, tgt, alt):
        if n == 1:
            return [[src, tgt]]
        return recurse(n-1, src, alt, tgt) + [[src, tgt]] + recurse(n-1, alt, tgt, src)
    return recurse(num_rings, 0, 1, 2)

@enable_executor_hook
def compute_tower_hanoi_wrapper(executor, num_rings):
    pegs = [list(reversed(range(1, num_rings + 1)))
            ] + [[] for _ in range(1, NUM_PEGS)]

    result = executor.run(functools.partial(compute_tower_hanoi, num_rings))

    for from_peg, to_peg in result:
        if pegs[to_peg] and pegs[from_peg][-1] >= pegs[to_peg][-1]:
            raise TestFailure('Illegal move from {} to {}'.format(
                pegs[from_peg][-1], pegs[to_peg][-1]))
        pegs[to_peg].append(pegs[from_peg].pop())
    expected_pegs1 = [[], [], list(reversed(range(1, num_rings + 1)))]
    expected_pegs2 = [[], list(reversed(range(1, num_rings + 1))), []]
    if pegs not in (expected_pegs1, expected_pegs2):
        raise TestFailure('Pegs doesn\'t place in the right configuration')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('hanoi.py', 'hanoi.tsv',
                                       compute_tower_hanoi_wrapper))
