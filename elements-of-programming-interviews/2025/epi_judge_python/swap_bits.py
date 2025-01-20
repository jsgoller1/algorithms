from test_framework import generic_test


def swap_bits(x, i, j):
    i_mask, j_mask = (x & (1 << i)), (x & (1 << j))
    x = (x | (1 << j)) if i_mask else (x & ~(1 << j))
    x = (x | (1 << i)) if j_mask else (x & ~(1 << i)) 
    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
