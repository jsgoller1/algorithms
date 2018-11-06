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


class Solution:
    def myPow(self, x, n):
        if n == 0:
            return -1 if x < 0 else 1
        elif n > 0:
            return x*self.myPow(x, n-1)
        else:
            return round(1/x * self.myPow(x, n+1), abs(n))


if __name__ == '__main__':
    s = Solution()
    assert s.myPow(0, 0) == 0**0
    assert s.myPow(10, 0) == 10**0
    assert s.myPow(100, 230) == 100 ** 230
    assert s.myPow(-100, 230) == -100 ** 230
    assert s.myPow(100, -230) == 100 ** -230
    assert s.myPow(-100, -230) == -100**-230
