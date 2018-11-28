import random

"""
Pseudocode of the complete algorithm follows, where the arrays are zero-based:
i ← 1
while i < length(A)
    j ← i
    while j > 0 and A[j-1] > A[j]
        swap A[j] and A[j-1]
        j ← j - 1
    end while
    i ← i + 1
end while
"""


def insertion_sort(arr):
    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        i += 1
    return arr


if __name__ == '__main__':
    arr = [random.randint(-100, 100) for i in range(10)]
    print(arr)
    print(insertion_sort(arr))
    assert insertion_sort(arr) == sorted(arr)
