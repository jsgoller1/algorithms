from typing import List

from test_framework import generic_test

"""
For [1,1,1,1,1,5,10,25]
smallest is 21, largest is sum of arr (only one of each coin)

[5] -> can't make 1
[1] -> can't make 2
[2] -> can't make 1
[1,2] -> can't make 4
[1,1,1,1,1] -> 6

Brute force: try every val from 1 to sum(arr)
If we don't have 1, then 1
If we don't have 

Assume we sort first. With coins[0], we can make that val. With
coins[1] added, we can make the original, coins[2], and their sum. 



"""

def smallest_nonconstructible_value(A: List[int]) -> int:
    curr_min = 1
    for val in sorted(A):
        if val > curr_min:
            return curr_min
        curr_min = curr_min + val  
    return curr_min


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
