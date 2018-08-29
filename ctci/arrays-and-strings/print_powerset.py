"""
EPI 5.5

Implement a function that takes as input a set S of distinct elements, and
prints the powerset (set of all subsets, including [] and S itself) of S.

Solution:
The key to solving this problem is recognizing that the powerset P of a set S
contains 2^|N| subsets (where |N| is the number of elements in N); for some element
e in S, every set in P either contains e or it doesn't. Because of this, we can
represent every set R in P with binary strings pertaining to S - if the 5th element
of S is in R, then R[4] (zero-indexing) is '1'; otherwise it's '0'. Therefore,
a binary string of all 1s of length len(S) represets S, a string of all zeroes
represents the empty set, and all strings in between are the powerset.

The runtime of this algorithm is O(n^2) for a set of size n.
"""

def print_powerset(my_set):
    # Ignore trivial cases
    length = len(my_set)
    if length == 0:
        return []
    if length == 1:
        return [[], my_set]
    # Create zero and longest 1-string using generators; initially append
    # the zero, and append the max before returning
    zero = ''.join(['0' for bit in range(0,length)])
    maximum = ''.join(['1' for bit in range(0,length)])
    bin_strings = [zero]
    count = 1
    # Loop through all the values our string could take by converting
    # decimal values to binary, and return them.
    while count < int(maximum, 2):
        bin_strings.append(bin(count)[2:].zfill(len(maximum)))
        count += 1
    bin_strings.append(maximum)

    for bin_string in bin_strings:
        subset = []
        for index, val in enumerate(bin_string):
            if val == '1':
                subset.append(my_set[index])
        print subset

if __name__ == "__main__":
    my_set = [0,5,11,33,55,6]
    print "set: ", my_set
    print_powerset(my_set)
