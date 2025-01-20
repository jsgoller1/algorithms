from typing import List

from test_framework import generic_test

def generate_all_perms():
    output = []
    def recurse(curr):
        if len(curr) == 4:
            output.append(curr)
        for i in range(1,5):
            if i not in curr:
                recurse(curr + [i])
    recurse([])
    return output
#print(sorted(generate_all_perms()))

def next_permutation(perm: List[int]) -> List[int]:
    for i in range(len(perm)-2, -1, -1):
        # Find the first correctly sorted adjacent numbers
        if perm[i] < perm[i+1]:
            lowest = perm[i+1]
            lowest_i = i+1
            # Look for the lowest thing to the right of the correctly
            # sorted pair we can swap the lesser element with 
            for j in range(i+1, len(perm)):
                if perm[i] < perm[j] <= lowest:
                    lowest = perm[j]
                    lowest_i = j 
            perm[i], perm[lowest_i] = perm[lowest_i], perm[i]
            # then sort everything after the swap point
            return perm[:i+1] + list(sorted(perm[i+1:]))
    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
