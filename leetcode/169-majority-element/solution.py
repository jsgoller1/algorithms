from collections import Counter


def majority(arr, lo, hi):
    if lo == hi:
        return arr[lo]
    mid = (hi+lo)//2
    lo_majority = majority(arr, lo, mid)
    hi_majority = majority(arr, mid+1, hi)

    # if both have same majority, then return it
    if lo_majority == hi_majority:
        return lo_majority
    # Otherwise, count the occurrences and return the best
    return Counter(arr[lo:hi+1]).most_common(1)[0][0]


cases = [
    ([3, 3, 4], 3),
    ([2, 2, 1, 1, 1], 1),
    ([1, 2, 1, 2, 1], 1),
    ([1, 1, 1, 2], 1),
]

for arr, expected in cases:
    actual = majority(arr, 0, len(arr)-1)
    assert actual == expected, f"{arr}: {expected} != {actual}"
