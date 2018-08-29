
"""
The pairity of a sequence of bits is 1 if the number of bits set to 1 in the
sequence is odd, and 0 otherwise. Given a binstring, compute the pairity. By
convention, a zero-length string's parity is 0.
"""
import library
import sys

def compute_parity(string):
    parity = False
    ones = 0
    for bit in string:
        if bit == '1':
            parity = not(parity)
            ones += 1
    print int(parity), ones

if __name__ == '__main__':
    string = library.generate_binstring()
    print string
    compute_parity(string)
