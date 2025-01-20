from test_framework import generic_test

"""
Multiply nonnegative integers. Can use loops, assignment, bool operations, and equality tests. 
Cannot increment, decrement, or use < or >.

- Multiplication is iterative addition. 
- Can we add a number to itself (i.e. x2) once for each bit set in 
  the second number? Don't think so (because then x * 10101 == x * 111), 
- Adding can be done as ripple-carry. 

lets say we have x * 11 (3). x * 10 = x << 1.  x * 1 = x. So x * 11 = (x << 1 + x)
so what about 100 (4) * x? that's (x << 2) + 0 + 0. 5 * 4 = 20, and 5 << 2

So we can iteratively add shifted versions of x to itself to get the result. 
Optimization: detect whichever is smaller based on highest set MSB, multiple by the smaller 

"""
def get_larger_smaller(x, y):
    xc, yc = x, y
    while x and y:
        x >>= 1
        y >>= 1
    return (xc, yc) if x else (yc, xc)

def add(x, y):
    """
    Bit is 0 if both bits are equal, 1 if not equal (xor)
    new carry is 1 if AND of both bits 
    Old bit |= carry  
    """
    place = 1
    total = 0 
    carry = 0 
    while x or y or carry:
        x_bit, y_bit = (x & 1), (y & 1)
        # Bit is set if x,y, or carry was set, or if all were set
        bit_state = x_bit ^ y_bit ^ carry
        # New carry is 1 if 2 or more of the above were set 
        new_carry = (x_bit & y_bit) | (x_bit & carry) | (y_bit & carry)
        if bit_state:
            total |= place 
        place <<= 1
        x>>=1
        y>>=1
        carry = new_carry
    return total 

def multiply(x: int, y: int) -> int:
    rsum = 0
    x, y = get_larger_smaller(x, y)
    while y: 
        if y & 1:
            rsum = add(rsum, x) 
        x <<= 1
        y >>= 1
    return rsum 

"""
for case in [
    (5, 0),
    (5, 1),
    (0, 0),
    (100, 1),
    (100, 100)
]:
    x, y = case 
    assert add(x,y) == x+y, f"{x,y}: {add(x,y)} != {x+y}"
    assert multiply(x,y) == x*y, f"{x}, {y}: {multiply(x,y)} != {x*y}"

"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('primitive_multiply.py',
                                       'primitive_multiply.tsv', multiply))
