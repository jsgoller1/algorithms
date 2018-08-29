import random

"""
An n-free binary list is a list of binary strings in which there is no string
contains n consecutive  1s or 0s.

Write a function that takes integers n and m as input, and returns all n-free
strings of length m (assume m can be any size but for testing doesn't need to
be larger than 10).
"""

def generate(length): # length is m
    # Ignore trivial cases
    if length == 0:
        return []
    if length == 1:
        return ["0", "1"]
    # Create zero and longest 1-string using generators; initially append
    # the zero, and append the max before returning
    zero = ''.join(['0' for bit in range(0,length)])
    maximum = ''.join(['1' for bit in range(0,length)])
    strings = [zero]
    count = 1
    # Loop through all the values our string could take by converting
    # decimal values to binary, and return them.
    while count < int(maximum, 2):
        print count
        strings.append(bin(count)[2:].zfill(len(maximum)))
        count += 1
    strings.append(maximum)
    return strings

def validate(strings, free_size):
    # Ignore trivial cases
    if strings == []:
        return strings
    if len(strings[0]) < free_size:
        return strings
    zeros = ''.join(['0' for bit in range(0,free_size)])
    ones = ''.join(['1' for bit in range(0,free_size)])
    results = []
    # Loop through and strip out strings with n consecutive 1s and zeros
    for each in strings:
        if (zeros not in each) and (ones not in each):
            results.append(each)
    return results

# This example run generates all lists of strings of length 4 that are 3-cube free
if __name__ == '__main__':
    m = random.randint(1,10)
    n = random.randint(1,m)
    strings = generate(m)
    print "All strings of length " + str(m) + ":"
    print strings
    print "Stripping out strings with " + str(n) + " ones and zeroes:"
    print validate(strings, n)
