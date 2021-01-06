import random

"""
Wikipedia:

algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)

algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo
    for j := lo to hi - 1 do
        if A[j] < pivot then
            if i != j then
                swap A[i] with A[j]
            i := i + 1
    swap A[i] with A[hi]
    return i

Sorting the entire array is accomplished by quicksort(A, 0, length(A) - 1).
"""

def quicksort(arr, low, high):
  if low < high:
    p = partition(arr, low, high)
    print(arr)
    quicksort(arr, low, p-1)
    quicksort(arr, p+1, high)

def partition(arr, low, high):
  pivot = arr[high]
  i = low
  print("partitioning from arr[{0}] to arr[{1}], pivot: {2}".format(low,high,pivot))
  for j in range(low, high):
    if arr[j] < pivot:
      if i != j:
        print("Swapping arr[{0}] = {1} with arr[{2}] = {3} ({3} less than pivot)".format(i, arr[i], j, arr[j]))
        arr[i], arr[j] = arr[j], arr[i]
      i+=1
  print(numbers)
  print("Setting pivot; swap arr[{0}] = {1} with arr[{2}] = {3}".format(i, arr[i], high, arr[high]))
  arr[i], arr[high] = arr[high], arr[i]
  print(numbers)
  print("="*20)
  return i

if __name__ == '__main__':
  numbers = [random.randint(-100,100) for i in range(20)]
  print(numbers)
  expected = sorted(numbers)
  quicksort(numbers, 0, len(numbers)-1)
  print(expected)
  print(numbers)
  assert numbers == expected
