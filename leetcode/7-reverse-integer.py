"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
For the purpose of this problem, assume that your function returns
0 when the reversed integer overflows.
---------------------------------------
Input: Integer
Output: Intger

- There is probably a dumb solution to this where we cast to a string,
reverse, and cast back to an int; we will try this first to see if it passes.
  - We need to be careful about the - symbol
- A more challenging version would be to actually reverse the bits in C.
- What weird edge cases could exist here?

"""


class Solution(object):
    def reverse(self, x):
        if x < 0:
            string = str(x)[1:]
            sign = -1
        else:
            string = str(x)
            sign = 1

        solution = int(string[::-1]) * sign
        if not ((-2**31) <= solution <= (2**31 - 1)):
            return 0
        return solution


if __name__ == '__main__':
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(666) == 666
    assert s.reverse(0) == 0
    assert s.reverse(230) == 32
    assert s.reverse(-231) == -132
    assert s.reverse(900000) == 9
