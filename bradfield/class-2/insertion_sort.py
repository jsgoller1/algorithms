import cProfile
import io
import pstats
import random

ARR_SIZE = 10000000
HUGE_ARR_SIZE = 1000000000


def insertion_sort(arr, in_place=False):
    # Note: in real life, I would write two separate functions - one that
    # returns an array and one that is in-place. For brevity, I'm using one
    # function with an argument that modifies the return type.
    if not in_place:
        sorted_arr = arr.copy()
    else:
        sorted_arr = arr

    # do actual sorting
    sorted_arr = sorted(sorted_arr)

    if not in_place:
        return sorted_arr


def timed_insertion_sort(arr):
    pr = cProfile.Profile()
    pr.enable()
    insertion_sort(arr, True)
    pr.disable()

    # Get profiling information
    stats = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=stats).sort_stats(sortby)
    ps.print_stats()

    return stats


def print_stats(stats_string):
    print(stats_string.getvalue())
    print("-"*100)


if __name__ == '__main__':
    # Base cases
    assert insertion_sort([], ) == sorted([])
    assert insertion_sort([1]) == sorted([1])

    # Pre-sorted array case
    pre_sorted = sorted([i for i in range(ARR_SIZE)])
    pre_sorted_timed = pre_sorted.copy()
    assert insertion_sort(pre_sorted) == pre_sorted
    print_stats(timed_insertion_sort(pre_sorted_timed))

    # Completely unsorted array case
    reversed_sorted = list(reversed(sorted([i for i in range(ARR_SIZE)])))
    reversed_sorted_timed = reversed_sorted.copy()
    assert insertion_sort(reversed_sorted) == sorted(reversed_sorted)
    print_stats(timed_insertion_sort(reversed_sorted_timed))

    # Very large case
    huge_arr = random.shuffle([i for i in range(HUGE_ARR_SIZE)])
    print_stats(timed_insertion_sort(huge_arr))

