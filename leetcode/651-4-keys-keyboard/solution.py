"""
Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.
Key 2: (Ctrl-A): Select the whole screen.
Key 3: (Ctrl-C): Copy selection to buffer.
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A'
you can print on screen.

Example 1:
Input: N = 3
Output: 3
Explanation:
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A

Example 2:
Input: N = 7
Output: 9
Explanation:
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V

Note:
- 1 <= N <= 50
- Answers will be in the range of 32-bit signed integer.
==========================================================================
- In: int, number of keys we can press
- Out: int, maximum char count that can be printed to the screen

- Found this problem with "dynamic programming" tag.
- Base case is N < 4; press A 4 times
- Ctrl-A / Ctrl-C / Ctrl-V takes whatever we had at n-3 and doubles it
- We can press Ctrl-V multiple times without re-copying.
- We should never Ctrl-AVC on an empty screen; if we ever execute it, we
will always paste at least one character, so there is no reason to press A again
once the sequence is completed.
- f(N) = max(f(n-3)*2, f(n-1)+1). f(n) = n if n < 5.
ex: f(10) = max(f(7)*2, f(9)+1)
  - this doesn't work because we need to keep track (recursively) of what the
  paste buffer was on those steps; we would always pick ctrl-V over pressing A.
  - Should we save a tuple representing (amount, pastebuffer) or can we implicitly / recursively
  derive the last valid paste buffer without using extra space?
  - what value is in the paste buffer?
    - last value of n-3 last time we executed the sequence
    - let's see if we can just store tuples at first and then define recursively if a pattern emerges
  - Tuples didn't work cleanly / got ugly
  - How can we determine what was in the paste buffer for the n-1th operation

- At each step, you can do one of four things:
  - A: n-1 + 1 chars
  - CA: n-1 chars
  - CC: n-1 chars
  - CV: n-1 + PB chars
- How do we determine what PB chars is?
  - PB is either n-3 or whatever it was for n-1

- Paste buffer for 1 - 3 is 0. For 4 it can be 1, but that won't work for the maximum
- Is this like the array roll-forward problem?

N   Val   Note
1    1    A
2    2    A x2
3    3    A x3
4    4    A x4
5    5    A x5
6    6    several; A x6; A x2, copy 2, CV x2; A x3, copy 3, CV x1
7    9    A x3, copy 2 and CV x2
8    12   several; A x4, copy 4, cv x2; A x3, copy 3, cv x3
9    16   A x4, copy 4, cv x 3
10   20   4 x 5 or 5 x 4
11   26   9 x 3
12   36   12 x 3 or 9 x 4, need to beat 48 next
13   48   16 x 3 or 12 x 4, need to beat 64 next
14   64   16 x 4, need to beat 80 next
15

15:
72 = 36 x2
78 = 26 x3
80 = 20 x4
80 = 16 x5
---------
14:
54 = 26 x 2
60 = 20 x 3
64 = 16 x 4
60 = 12 x 5
------
13:
40 = 20 x 2
48 = 16 x 3
48 = 12 x 4
45 = 9 x 5
-----
12:
32 = 16 x 2
36 = 12 x 3
36 = 9 x 4
30 = 6 x 5

If N < 6, return N.
Else look back at N-3 iteratively still it starts decreasing

"""

class Solution(object):
    def maxA(self, n):
        cache = {i:i for i in range(6)}
        for i in range(6, n+1):
          count = 2
          curr = i-3
          currMax = cache[curr] * count
          while cache[(curr-1)] * (count+1) >= currMax:
            count += 1
            curr -= 1
            currMax = cache[curr] * count
          cache[i] = currMax
        return cache[n]

    def cachePrint(self, cache):
      for key in cache:
        print("{0}: {1}".format(key, cache[key]))
      print("="*15)



if __name__ == '__main__':
  s = Solution()
  assert s.maxA(3) == 3
  assert s.maxA(7) == 9
  assert s.maxA(7) == 9
  assert s.maxA(11) == 27

