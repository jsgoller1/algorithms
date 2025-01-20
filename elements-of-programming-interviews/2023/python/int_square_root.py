from test_framework import generic_test


"""
Adapt binary search
if m*m > k, choose lower, no solution
if m*m == k, return m
if m*m < k choose upper, but m might be candidate
"""


def square_root(k: int) -> int:
    lo, hi = 0, k
    # ensures we examine all possible candidates
    while lo <= hi:
        m = (hi + lo) // 2
        if m*m > k:
            # m is definitely not a solution
            hi = m-1
        elif m*m == k:
            return m
        else:  # m*m < k
            # m might be a solution; we exclude it for
            # now, but hi will pick it up when hi < lo
            # if it's the best solution.
            lo = m+1
    return hi


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
