def quicksort(arr, lo, hi):
    while lo < hi:
        mid = partition(arr, lo, hi)
        quicksort(arr, lo, mid - 1)
        quicksort(arr, mid + 1, hi)


def partition():
    pass
