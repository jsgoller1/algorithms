from test_framework import generic_test


def add(x: int, y: int) -> int:
    val = x ^ y
    carry = (x & y) << 1
    while carry:
        x = val
        y = carry
        val = x ^ y
        carry = (x & y) << 1
    return val


def multiply(x: int, y: int) -> int:
    product = 0
    while y:
        if (y & 1):
            product += x
        x <<= 1
        y >>= 1
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
