"""
Statement: Sort an array with quicksort and try different partitioning strategies.
Input: List of Ints; may be empty, singleton or very large
Out: List of Ints
-----------
Understand:
- Problem statement calls for quicksort.
- Quicksort (wikipedia):
    1. Pick an element, called a pivot, from the array.
    2. Partitioning: reorder the array so that all elements with values less than
       the pivot come before the pivot, while all elements with values greater than
       the pivot come after it (equal values can go either way). After this partitioning,
       the pivot is in its final position. This is called the partition operation.
    3. Recursively apply the above steps to the sub-array of elements with smaller 
       values and separately to the sub-array of elements with greater values.
- We should be able to easily change which partitioning strategy we use in the implementation.
- Skiena points out that some inputs (which?) can be pathological, but that pre-shuffling our input takes care of most of these
----------
Review 
- This algorithm does poorly when non-unique elements are in the array. Consider this alternative:
    - When partitioning, divide the array into four portions: greater than partition, equal to partition, and less than partition
    - Put the partition in the middle (i.e. middle index) of the array. This divides the array into a left unknown and right unknown portion.
    - Then for each element in each unknown portion:
        - If it's greater than the partition, put it to the right of the equal partition group.
        - If it's less, put it to the left.
        - If it's equal, put it adjacent to the partition.
    - Do this process recursively til there's no greater than / less than portions left.
"""
import random


def lomuto_partition(arr, low, high):
    """
    The Lomuto partition boils down to "pick a partition element,
    move everything smaller to the right of it, then swap it in at the end":
    """
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quicksort(arr, partition_fn, shuffle=False):
    if shuffle:
        # Skiena voice: "Hokay, so - what happens if we shuffle first?"
        # This can effectively eliminate some pathological cases of input.
        random.shuffle(arr)

    def sort(arr, low, high):
        if low < high:
            pivot = partition_fn(arr, low, high)
            sort(arr, low, pivot - 1)
            sort(arr, pivot + 1, high)

    sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    test_pairs = [
        ([], []),
        ([1], [1]),
        # Pathological case 1
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],),
        ([1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]),
        ([5, 1, 3, 4, 5, 10], [1, 3, 4, 5, 5, 10]),
    ]
    for pair in test_pairs:
        actual, expected = pair
        quicksort(actual, lomuto_partition)
        assert actual == expected
