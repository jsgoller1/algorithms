from test_framework import generic_test
from test_framework.test_failure import TestFailure

from string import digits

def decoding(s: str) -> str:
    decoded = []
    num = []
    for c in s: 
        if c in digits:
            num.append(c)
        else: 
            count = int(''.join(num))
            decoded.append(c * count)
            num = []
    return ''.join(decoded)


def encoding(s: str) -> str:
    if not s:
        return ''
    curr = s[0]
    count = 0
    encoded = []
    for c in s: 
        if c == curr:
            count += 1 
        else:
            encoded.append(str(count)+curr)
            curr = c 
            count = 1
    encoded.append(str(count)+curr)   
    return ''.join(encoded)


from collections import Counter

def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure(f'Decoding failed:\n{Counter(decoding(encoded))}\n!=\n{Counter(decoded)}')
    if encoding(decoded) != encoded:
        raise TestFailure(f'Encoding failed:\n{encoding(decoded)}\n!=\n{encoded}')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('run_length_compression.py',
                                       'run_length_compression.tsv',
                                       rle_tester))
