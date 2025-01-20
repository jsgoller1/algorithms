from test_framework import generic_test


def fibonacci_iterative_no_cache(n: int) -> int:
    if n < 2:
        return n
    n_2 = 0
    n_1 = 1
    total = 1
    for i in range(2, n+1):
        total = n_1 + n_2
        n_2 = n_1
        n_1 = total
    return total


def fibonacci_recursive_with_cache(n: int) -> int:
    if n < 0:
        raise ValueError("n must be nonnegative.")
    cache = {0: 0, 1: 1}

    def recurse(n):
        if n not in cache:
            ans = recurse(n-1) + recurse(n-2)
            cache[n] = ans
        return cache[n]

    return recurse(n)


def fibonacci(n):
    ans1 = fibonacci_iterative_no_cache(n)
    ans2 = fibonacci_recursive_with_cache(n)
    assert ans1 == ans2, f"{n}: {ans1} != {ans2}"
    return ans1


if __name__ == '__main__':
    cases = [
        (0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)
    ]
    for n, expected in cases:
        actual = fibonacci(n)
        assert actual == expected, f"{n}: {actual} != {expected}"

    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
