from test_framework import generic_test

"""
- Weight of an integer is num of bits set
- fiddling with MSB creates biggest difference 
- cases:
  - 01 (1) -> 10 (2)
  - 101 (5) -> 110 (6), not 11 (3)
  - 1111 (15) -> 10111 (23)
- seems like best case is "move first bit we can one to the left" 

so:
- find lsb's position, call it i
- set ith bit to 0 (xor)
- xor subsequent bits until the bit is set?

Wrong - seems like we do want to do something to the least significant bit, just not always move it forward. 
If we can rshift it one, that is best: minimal distance involves setting the bit closest to it that we can,
- any to the right are better than any to left.

"""

def closest_int_same_bit_count(x: int) -> int:
    if x == 0:
        return x
    bitmask = 1
    # Find first instance of 01 or 10
    while (bitmask << 1 & x == 0) == (bitmask & x == 0):
        bitmask <<= 1
    x ^= (bitmask << 1 | bitmask)
    return x 

for x, expected in [
    (0b1, 0b10),
    (0b101, 0b110),
    (0b1111, 0b10111),
    #(0b110000, 0b1010000),
    #(0, 0)
]:
    actual = closest_int_same_bit_count(x)
    assert actual == expected, f"{bin(x)}: {bin(actual)} != {bin(expected)}"

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('closest_int_same_weight.py',
                                       'closest_int_same_weight.tsv',
                                       closest_int_same_bit_count))
