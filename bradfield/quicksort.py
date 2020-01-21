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
"""



def lomuto_partition():
    pass

def hoare_partition():
    pass

def sort(arr, partition_fn):
    return arr

def quicksort(arr, partition_fn, shuffle=True):
    if shuffle:
        # do shuffling here
        pass
    return sort(arr, partition_fn)

if __name__ == '__main__':
    test_arrs = [
        [],
        [1]
        [6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5, 6]
        [1, 1, 1, 1, 1, 1],
        [5, 1, 3, 4, 5, 10],
    ]
    for arr in test_arrs:
        assert quicksort(arr, lomuto_partition) == sorted(arr)
        assert quicksort(arr, hoare_partition) == sorted(arr)