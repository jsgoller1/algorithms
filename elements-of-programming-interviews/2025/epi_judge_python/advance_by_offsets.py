from typing import List

from test_framework import generic_test

"""
For a board to be unwinnable, we have to have a situation where no cell can reach past a certain point
i.e.: 
[1,0,X]

Start from end; mark last cell as X.
Go to the next cell from the right. If cell can reach end, it's the new end

3,3,1,0,2,0,1
0,0,0,5
1,1,1,1,1
"""

def can_reach_end(A: List[int]) -> bool:
    end = len(A)-1
    curr = end-1
    while 0 <= curr: 
        if end <= curr + A[curr]:
            end = curr 
        curr -= 1
    return end == 0 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
