from typing import Iterator, List

from test_framework import generic_test

from heapq import heappush, heappop

def online_median(sequence: Iterator[int]) -> List[float]:
    medians, lower, upper, = [],[],[]
    for new in sequence:
        # Add new element
        if lower and new <= -lower[0]:
            heappush(lower, -new)
        else:
            heappush(upper, new)

        # balance heaps 
        big, small = (upper, lower) if (len(upper) > len(lower)) else (lower, upper)
        while len(big)-len(small) > 1:
            heappush(small, -heappop(big))

        if len(upper) == len(lower):
            median = (-lower[0] + upper[0])/2 
        else: 
            median = -lower[0] if len(lower) > len(upper) else upper[0]
        medians.append(median)

    return medians 


def online_median_wrapper(sequence):
    return online_median(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('online_median.py', 'online_median.tsv',
                                       online_median_wrapper))
