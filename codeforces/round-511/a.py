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


def make_indivisible(x, y, z):
    arr = sorted([int(x), int(y), int(z)])
    c = arr[0]
    b = arr[1]
    a = arr[2]

    while (((a % 3) == 0) and ((b % 3) == 0) and ((c % 3) == 0)):
        if (a % 3) == 0:
            a += 2
            b -= 1
            c -= 1
        if (b % 3) == 0:
            a += 1
            b -= 1
        if (c % 3) == 0:
            a += 1
            c -= 1

    return a, b, c


def break_down(n):
    if (n % 3 == 0):
        return make_indivisible(n / 3, n / 3, n / 3)
    if ((n + 1) % 3 == 0):
        n += 1
        return make_indivisible((n / 3) - 1, n / 3, n / 3)
    if ((n + 2) % 3 == 0):
        n += 2
        return make_indivisible((n / 3) - 2, n / 3, n / 3)


if __name__ == '__main__':
    inline = input()
    while inline != '':
        a, b, c = break_down(int(inline))
        print("{0} {1} {2}".format(a, b, c))
        inline = input()
