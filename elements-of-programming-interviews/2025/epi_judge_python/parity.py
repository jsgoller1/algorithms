from test_framework import generic_test

# For many 64-bit words combined into 1 word, 
# we can just XOR them all together:
# two 0s have no impact on parity, and two 1s preserve parity
# but a 1 and a 0 mean we have a 1 that needs to be dealt with

def parity(x: int) -> int:
    parity = True
    while x:
        parity = (not parity) if x & 1 else (parity)
        x >>= 1
    return 1 if not parity else 0 


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
