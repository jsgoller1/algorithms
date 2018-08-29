from test_framework import generic_test


#!/bin/python

"""
1.1 - How do you compute the parity (1 if odd number of set bits, 0 if even) for a very large number of 64-bit words?
"""


def slowest_parity(val):
    """
    parity(): determine bit by bit if number has parity
    """
    bit_list = list(bin(val)[2:])
    return bit_list.count('1') % 2


def bf_parity(val):
    """
    parity(): determine parity by looking up each 4 bits via a cache;
    the text takes a similar approach, but caching 16-bit words instead of 4;
    this approach is 1 microsecond faster than the following appoach.
    """
    hex_pair = {'1': 1, '0': 0, '3': 0, '2': 1, '5': 0, '4': 1,
                '7': 1, '6': 0, '9': 0, '8': 1, 'a': 0, 'c': 0, 'b': 1, 'e': 1, 'd': 1, 'f': 0}
    pairsum = 0
    for hchar in hex(val)[2:]:
        pairsum += hex_pair[hchar]
    return pairsum % 2


def parity(val):
    """
    parity(): determine parity by successively deleting the lowest set bit until the value is zero.
    Worst case is slower than slow_parity() but will be faster on average, but will be
    faster for all values where there are less than 16 bits set.
    """
    is_parity = 0
    while val:
        is_parity ^= 1  # flips back and forth
        val &= val - 1  # x-1 unsets lowest set bit and flips all 0'd bits before it, so all higher bits are preserved
    return is_parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
