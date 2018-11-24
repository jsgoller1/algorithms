"""
Reverse bits of a given 32 bits unsigned integer.

Example:
Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100,
             return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
- If this function is called many times, how would you optimize it?
---------------------------------------------------------------------
In: Integer
Out: Integer

- The simplest solution to this is just to cast the integer to a binstring,
reverse it, and cast it back to an int.

- A more C-like way to do it would be:
  - have two ints, input and output
  - while input > 0:
    - left shift output by 1
    - 1 AND input, output = 1 OR output
    - right shift input by 1
 to right shift while the original int is > 0;
if the rightmost bit before the shift was set, set the rightmost bit
"""


class Solution:
    def reverseBits(self, n):
        out = 0
        remaining = 32
        while n > 0:
            out = out << 1
            if n & 1:
                out |= 1
            n = n >> 1
            remaining -= 1
        return out << remaining

    def reverseBitsPython(self, n):
        n = bin(n)[2:]
        n = n.zfill(32)
        n = n[::-1]
        return int(n, 2)


if __name__ == '__main__':
    s = Solution()
    assert s.reverseBits(43261596) == 964176192
