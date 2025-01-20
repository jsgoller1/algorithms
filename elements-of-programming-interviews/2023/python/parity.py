from test_framework import generic_test
from typing import List


def parity(x: int) -> int:
    parity = False
    while (x):
        if (x & 1):
            parity = not parity
        x >>= 1
    return parity


def collective_parity(vals: List[int]) -> int:
    collected = vals[0]
    for val in vals[1:]:
        collected ^= val
    return parity(collected)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
