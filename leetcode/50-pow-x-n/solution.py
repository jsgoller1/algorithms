"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Constraints:
- -100.0 < x < 100.0
- n is a 32-bit signed integer, within the range [−231, 231 − 1]

Input: float (base), signed int (power)
Output: float (result)
-----------------------------------------------------------------
- We can write a simple recursive implementation of this function
- Lots of downvotes? maybe it's too easy?
"""
import math


def myPowIterative(x, n):
    result = 1
    if n > 0:
        for _ in range(n):
            result *= x
    elif n < 0:
        for _ in range(n, 0):
            result /= x
    return result


class Solution:
    def pow(self, x, n):
        if n not in self.cache:
            if (n % 2) == 1:
                m = (n-1)//2
                self.cache[n] = x * self.pow(x, m) * self.pow(x, m)
            else:
                self.cache[n] = self.pow(x, n // 2) * self.pow(x, n // 2)
        return self.cache[n]

    def myPow(self, x, n):
        if n == 0:
            return 1 if x >= 0 else - 1
        if x == 0:
            return 1
        if n < 0:
            n *= -1
            x = 1 / x  # possible zero div
        self.cache = {1: x}
        return self.pow(x, n)


if __name__ == '__main__':
    # NOTE: Python does imprecise fraction calculations; this program passes the (highly downvoted) leetcode question, but fails here
    s = Solution()
    tests = [(0.00001, 2147483647), (0, 0), (10, 0), (100, 23),
             (-100, 23), (100, -23), (-100, -23)]
    for test in tests:
        print("Test: {0}".format(test))
        print(s.myPow(test[0], test[1]), test[0] ** test[1])
        assert s.myPow(test[0], test[1]) == test[0] ** test[1]
