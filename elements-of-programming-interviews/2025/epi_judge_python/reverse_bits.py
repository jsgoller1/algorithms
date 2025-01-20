from test_framework import generic_test

table = {
    0: 0,
    1: 8,
    2: 4,
    3: 12,
    4: 2,
    5: 10,
    6: 6,
    7: 14,
    8: 1,
    9: 9,
    10: 5,
    11: 13,
    12: 3,
    13: 11,
    14: 7,
    15: 15
}

def reverse_bits(x: int) -> int:
    low_bitmask = 15 
    result = 0 
    for _ in range(16):
        result <<= 4
        result |= table[x&low_bitmask]
        x >>= 4
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
