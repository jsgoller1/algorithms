def quicksort(arr, low, high):
  if low < high:
    p = partition(arr, low, high)
    #print("Recursively sorting: " + str(arr[low:p-1]))
    quicksort(arr, low, p - 1)
    #print("Recursively sorting: " + str(arr[p+1:high]))
    quicksort(arr, p+1, high)
  return arr

def partition(arr, low, high):
  print("Partitioning: " + str(arr))
  print("low: {0}, high: {1}".format(low,high))
  pivot = arr[high]
  print("pivot: " + str(pivot))
  i = low - 1
  print("i: " + str(i))
  for j in range(low, high):
    print("comparing {0} and {1}".format(arr[j], pivot))
    if arr[j] < pivot:
      i += 1
      print("swapping {0} and {1}".format(arr[i], arr[j]))
      swap(arr, i, j)
      print(arr)
  swap(arr, i+1, high)
  return i+1

def swap(arr, a, b):
  temp = arr[a]
  arr[a] = arr[b]
  arr[b] = temp

if __name__ == '__main__':
  arr = [1, 8, 7, 3, 10, 0, 4, 6, 9, 5, 2]
  #quicksort(arr, 0, len(arr) - 1)
  partition(arr, 0, 10)
  print(arr)
