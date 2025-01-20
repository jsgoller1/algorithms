from typing import Iterator, List

from test_framework import generic_test

"""
1,0,3,5,2,0,1
1,0.5,1,2,2,1.5,1

1 -> 1
0,| 1 -> .5
0,|1|,3 -> 1
0,1,| 3,5 -> 2
0,1,|2|,3,5 -> 2
0,0,1, | 2,3,5 -> 1.5
0,0,1,|1|,2,3,5 -> 1

if odd, middle element
if even, average of two innermost elements. 

brute force: insert, sort, calculate (nlogn)

if we kept the "smallest of the larger half" and "largest of the smaller half" elements, 
then we can just average them 
    - can probably look at size of greatests and leasts to determine if odd number or not 


"""
from heapq import heappush, heappop


def online_median(arr: Iterator[int]) -> List[float]:
    medians = []
    try:
        first = next(arr)
        medians.append(first)
        second = next(arr)

        left = [-first if first < second else -second]
        right = [first if first > second else second]
        medians.append((-left[0] + right[0])/2)
    except StopIteration:
        return medians

    for val in arr:
        # ensure every element in left is less than smallest
        # in right
        if val < right[0]:
            heappush(left, -val)
        else:
            heappush(right, val)

        # Ensure balance via shifting elements from one
        # heap to another (in order) if needed
        while len(left) - len(right) > 1:
            heappush(right, -heappop(left))
        while len(right) - len(left) > 1:
            heappush(left, -heappop(right))

        # Compute median depending on even/odd number of elements
        if len(right) == len(left):
            medians.append((-left[0] + right[0])/2)
        else:
            medians.append(-left[0] if len(left) > len(right) else right[0])
    return medians


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
