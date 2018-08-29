from test_framework import generic_test


def count_bits_alt(val):
    """
    count_bits - count all set bits in val
    """
    bits = 0
    for bit in bin(val):
        if bit == '1':
            bits += 1
    return bits


def count_bits(val):
    """
    count_bits_alt - count all set bits in val
    """
    return list(bin(val)).count('1')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("count_bits.py", 'count_bits.tsv',
                                       count_bits))
