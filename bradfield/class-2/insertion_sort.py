import cProfile
import io
import pstats

ARR_SIZE = 1000
HUGE_ARR_SIZE = 100000000


def insertion_sort(arr, in_place=False):
    # Note: in real life, I would write two separate functions - one that
    # returns an array and one that is in-place. For brevity, I'm using one
    # function with an argument that modifies the return type.
    if not in_place:
        sorted_arr = arr.copy()
    else:
        sorted_arr = arr

    # actual insertion sort code
    i = 0
    arr_len = len(sorted_arr)
    while i < arr_len:
        j = i
        while j > 0 and sorted_arr[j] < sorted_arr[j - 1]:
            sorted_arr[j], sorted_arr[j - 1] = sorted_arr[j - 1], sorted_arr[j]
            j -= 1
        i += 1

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
    assert insertion_sort([2, 0, 5, 8, 3, 1, 4, 7, 6, 9]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

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
    # Here is a weird way to build a large array; trying to instantiate an
    # array of HUGE_ARR_SIZE and shuffle it proved to be non-feasible,
    # but appending multiple smalller arrays seems to work.
    huge_arr = []
    while len(huge_arr) < HUGE_ARR_SIZE:
        huge_arr += [i for i in range(ARR_SIZE)]
    print_stats(timed_insertion_sort(huge_arr))

