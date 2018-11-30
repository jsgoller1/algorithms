"""
- start with i = 0
- from i to len(arr)-1:
  - get min
  - swap min with arr[i]
  - i++
"""
import random

def selection_sort(arr):
  for i in range(len(arr)):
    min_j = i
    for j in range(i, len(arr)):
      if arr[j] < arr[min_j]:
        min_j = j
    arr[i], arr[min_j] = arr[min_j], arr[i]

if __name__ == '__main__':
  arr = [random.randint(-100,100) for i in range(random.randint(10,20))]
  print(arr)
  print(sorted(arr))
  selection_sort(arr)
  print(arr)
  assert sorted(arr) == arr
