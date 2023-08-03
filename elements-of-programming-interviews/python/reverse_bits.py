from test_framework import generic_test


def reverse_bits(x: int) -> int:
    rev_x = 0
    for _ in range(64):
        rev_x <<= 1
        if (x & 1):
            rev_x |= 1
        x >>= 1
    return rev_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
