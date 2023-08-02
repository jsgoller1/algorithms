from test_framework import generic_test


def parity(x: int) -> int:
    parity = False
    while (x):
        if (x & 1):
            parity = not parity
        x >>= 1
    return parity


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
