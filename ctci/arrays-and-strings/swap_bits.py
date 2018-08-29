"""
Given a binary string of any length and two indices for that string,
write a program that will swap the bits at those indices.

The solution relies on some bitmath - if they're the same value, then swapping
them has no effect and we must detect that; otherwise XOR the bits with 1, which
will flip their value; we must create a string that has 1s in the right places.
"""

def swap_bits(binstring, idx1, idx2):
    # ignore trivial cases
    if len(binstring) < 2:
        print binstring
    # detect if the bits are the same
    if binstring[idx1] == binstring[idx2]:
        print binstring

    # Replace the appropriate places in the string with 1s, then convert
    # from list to string, then to int for binary operations
    flipping_list = ['0' for bit in range(0,len(binstring))]
    flipping_list[idx1] = '1'
    flipping_list[idx2] = '1'
    flipping_string = '0b'+''.join(flipping_list)
    flipping_val = int(flipping_string,2)

    # Cast binstring to int, xor with flipping string, print results
    base_val = int(binstring,2)
    result = base_val ^ flipping_val
    print "Indices to flip: " + flipping_string[2:]
    print "Original string: " + binstring
    print "Result: " + bin(result)[2:]


if __name__ == '__main__':
    swap_bits('00001111', 0, 7)
