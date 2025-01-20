from typing import List

from test_framework import generic_test

"""
If we sort the array first, then we know how 
long it is and what the max val is. 

[1,2,3,4,5,6,7,8]
[0,0]
[0]
[100]
[1,2,2,3,3,4]

Answer is between 0 and len(arr)
"""

def h_index(citations: List[int]) -> int:
    best = 0
    papers = 1
    citations.sort(reverse=True)
    for h in citations:
        best = papers if h >= papers else best
        papers += 1
    return best 



if __name__ == '__main__':
    exit(generic_test.generic_test_main('h_index.py', 'h_index.tsv', h_index))
