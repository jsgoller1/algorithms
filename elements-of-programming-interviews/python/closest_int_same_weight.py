from test_framework import generic_test


def closest_int_same_bit_count(x: int) -> int:
    original = x
    i = 0
    curr = prev = x & 1 != 0

    while (prev == curr):
        x >>= 1
        prev = curr
        curr = x & 1 != 0
        i += 1

    mask = (1 << i) | (1 << i-1)
    return original ^ mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
