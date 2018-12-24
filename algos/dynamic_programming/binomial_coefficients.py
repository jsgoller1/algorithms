"""
A program to calculate binomial coefficients. "Binomial
coefficients" are the positive integers that occur as coefficients
in the expanded sum of binomials of the form (x + y)^c. For example,
(x+y)^3 = x^3 + 3(x^2)y + 3x(y^2) + y^3; the binomial coefficients are
1-3-3-1, in that order. For more, see https://en.wikipedia.org/wiki/Binomial_theorem#Examples.
Ordering each row vertically from c=1 to c=n forms "Pascal's triangle".

Binomial coefficients can be used to solve the combinatorics problem "n choose k",
which asks "given n elements, how many different ways can k-sized unordered
subsets be selected?" The solution to n choose k is the x^k term in the binomial
expansion of (1 + x)^n. For example, to find 4 choose 2, start by expanding
(1+x)^4:
  1x^4 + 4x^3 + 6x^2 + 4x^1 + 1x^0

Then select the coefficient for the term x^2, which is 6. This means there are 6 ways to choose
2 items from a 4-item set, such as {1,2,3,4}: {1,2}, {1,3}, {1,4}, {2,4}, {2,3}, {3,4}.

We can compute (n choose k) directly: f(n,k) = n!/(k!(n-k)!). However, n! overflows
an 32-bit integer if n > 12 and a 64-bit integer if n > 20, so intermediate
calculations are problematic. (n choose k) can also be calculated recursively:
f(n,k) = f(n-1, k-1) + f(n-1,k) for all ints 1 <= k <= n - 1 (the recurrence
is related to the fact that each number in Pascal's triangle is the sum
of the two numbers above it). The base case for this recurrence is
(n choose 0), which is equal to (n choose n), or 1.

The solution below is adopted from Skiena in 8.1.
"""
import math
import random


def binomial_coefficient_direct(n, k):
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))


def binomial_coefficient_dp(n, k):
    if n < k:
        raise ValueError("n must be less than k.")
    if k == 0:
        return 1

    dp = [[0] * (n+1) for i in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(n+1):
        dp[i][i] = 1

    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][n-k]


if __name__ == '__main__':
    for i in range(10):
        n = random.randint(1, 20)
        k = random.randint(1, n)
        expected = binomial_coefficient_direct(n, k)
        actual = binomial_coefficient_dp(n, k)
        print("{0} choose {1}\n------\nactual: {2}\nexpected: {3}".format(n,
                                                                          k, actual, expected))
        assert actual == expected
