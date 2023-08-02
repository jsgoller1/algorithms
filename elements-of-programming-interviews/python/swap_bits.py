from test_framework import generic_test


def swap_bits_strings(x, i, j):
    """
    Different strategy; complicated binary operations can be hard to read
    and reason about, but python makes it easy to convert an integer to a list of bits,
    which we can then manipulate and recombine to an integer. 
    """
    bits = list(bin(x)[2:].zfill(64)[::-1])
    swapped = [val for val in bits]
    swapped[i] = bits[j]
    swapped[j] = bits[i]
    return int("".join(swapped[::-1]), 2)


def swap_bits(x, i, j):
    # Check if bits are different; if so, flip them both.
    if ((x >> i) & 1) != ((x >> j) & 1):
        mask = (1 << i) | (1 << j)
        x ^= mask
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
