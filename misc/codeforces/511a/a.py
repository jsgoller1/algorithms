"""
Statement

Given an integer n, split it into three numbers a,b,c such that a + b + c = n,
and none of a,b,c are divisible by 3.

Constraints:
3 <= n < 10**9

Input: Single integer
Output: a,b,c - if several solutions exist, any are acceptable

Examples:
in - 3
out - 1 1 1

in - 233
out - 77 77 99
----
Understand / Plan

- if n is itself divisible by 3, set a,b,c to n/3. Check if n/3 is divisible
by 3. if so, decrement a and b once, and increment c twice.

- if n is indivisible by 3, check n+1 and n+2. set n to the first one divisible by
3. set a,b,c to n/3, and decrement a by 1 or by 2 depending on whether we selected n+1 or
n+2. Then do the same procedure as above (sort of)

- a,b,c cannot be 0 (thought this was ok going in)
- to avoid a case where an int is zero, we should allow a to be the "accumulator"
and subtract from c and b while they are greater than 1. If we run into a case where a is a multiple
and b or c are 1, then we subtract 1 from a and add to b, then another from a and add to c.

- to avoid a situation where any of the initial values are 0:


- we have a common need here for a procedure f(a,b,c) that returns 3 numbers x,y,z whose sum
is a+b+c, but who are indivisible by 3. Call f make_invisible():

make_indivisible(a,b,c):
  arr = [a,b,c].sort()
  c = arr[0]
  b = arr[1]
  a = arr[2]

  while(a%3 != 0 && b%3 != 0 && c%3 != 0):
    if a%3 == 0:
      a+=2
      b-=1
      c-=1
    if b%3 == 0:
      a+=1
      b-=1
    if c%3 == 0:
      a+=1
      c-=1

  return a,b,c

3,4,4
6,3,3
3,3,3
"""
import sys


def make_indivisible(x, y, z):
    arr = sorted([int(x), int(y), int(z)])
    c = arr[0]
    b = arr[1]
    a = arr[2]

    while (a % 3) == 0 or (b % 3) == 0 or (c % 3) == 0:
        if (a % 3) == 0:
            if b > 1:
                b -= 1
                a += 1
            elif c > 1:
                c -= 1
                a += 1
            else:
                a -= 1
                b += 1
        if (b % 3) == 0:
            b -= 1
            a += 1
        if (c % 3) == 0:
            c -= 1
            a += 1

    return a, b, c


def break_down(n):
    if (n % 3 == 0):
        return make_indivisible(n / 3, n / 3, n / 3)
    if ((n - 1) % 3 == 0):
        n -= 1
        return make_indivisible((n / 3) + 1, n / 3, n / 3)
    if ((n - 2) % 3 == 0):
        n -= 2
        return make_indivisible((n / 3) + 1, (n / 3) + 1, n / 3)


if __name__ == '__main__':
    """
    i = 3
    while i < 10 ** 9:
        a, b, c = break_down(i)
        try:
            assert a + b + c == i
            assert a % 3 != 0
            assert b % 3 != 0
            assert c % 3 != 0
        except AssertionError:
            print(a, b, c, i)
            sys.exit(0)
        i += 1
    """

    while True:
        try:
            inline = input()
        except EOFError:
            sys.exit(0)
        a, b, c = break_down(int(inline))
        print("{0} {1} {2}".format(a, b, c))
