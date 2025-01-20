from typing import List

from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    table = [False for i in range(n+1)]
    primes = []
    for i in range(2, n+1):
        if table[i] == True:
            continue
        primes.append(i)
        for j in range(0, n+1, i):
            table[j] = True
    return primes


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
