from typing import List

from test_framework import generic_test

"""
GPT's suggestion using a sliding window on the combined array
"""

from collections import Counter
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    # Merge arrays with their source information
    merged = sorted((val, i) for i, arr in enumerate(sorted_arrays) for val in arr)
    if not merged:
        return None
    l = r = 0
    best = float('inf')
    counts = Counter()
    arrays_count = len(sorted_arrays)

    while r < len(merged):
        # Expand the window by adding the right element
        _, source = merged[r]
        counts[source] += 1

        # Shrink the window from the left as long as it's valid
        while len(counts) == arrays_count:
            best = min(best, merged[r][0] - merged[l][0])
            print(f"Best: {best} ({l},{r})")
            _, left_source = merged[l]
            counts[left_source] -= 1
            if counts[left_source] == 0:
                del counts[left_source]
            l += 1
        r += 1

    return best 

for case in [
    [
        # [(-5,2)(1,0),(1,1),(4,2),(16,0)]
        [1,16],
        [2],
        [-5,4],
        3 # [2,3]
    ],
    [
        [5,10,15],
        [3,6,9,12,15],
        [8,16,24],
        1 # [15,16]
    ],
    [
        [15,16,17],
        [0,16,25],
        [1,2,3,4,5,6,17],
        1 # [16,17]
    ],
    [
        [1],
        [2],
        [3],
        2 # [1,3]
    ]
]:
    arr1, arr2, arr3, ans = case
    arrs = [arr1, arr2, arr3]
    actual = find_closest_elements_in_sorted_arrays(arrs)
    assert ans == actual, f"{arrs}: {actual} != {ans}"
    print("---")
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('minimum_distance_3_sorted_arrays.py',
                                       'minimum_distance_3_sorted_arrays.tsv',
                                       find_closest_elements_in_sorted_arrays))
