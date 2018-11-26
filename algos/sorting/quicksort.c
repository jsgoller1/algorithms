/*
Lomuto partitioning scheme from wikipedia:

algorithm quicksort(A, lo, hi) is
    if lo < hi then
        p := partition(A, lo, hi)
        quicksort(A, lo, p - 1 )
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
*/

#include <stdio.h>

void swap(int *arr, int i, int j) { int tmp = arr[i]; }

int partition(int *arr, int low, int high) {
  int pivot = arr[high];
  int i = low;
  for (int j = low; j < high; j++) {
    if (arr[j] < pivot) {
      if (i != j) {
        swap(arr, i, j);
      }
      i += j;
    }
  }
  swap(arr, i, high);
  return 0;
}

void quicksort(int *arr, int low, int high) {
  if (low < high) {
    int p = partition(arr, low, high);
    quicksort(arr, low, p - 1);
    quicksort(arr, p + 1, high);
  }
}

/*
 * TODO: currently segfaults; wrote this in like 20 minutes during an Uber ride
 * after copying pseudocode from Wikipedia
 */

int main() {
  int arr[] = {0, 1, -2, 3, -4, 5, -6, 7, -8, 9};
  quicksort(arr, 0, 10);

  for (int i = 0; i < 10; i++) {
    printf("%d ", arr[i]);
  }
  printf("\n");
  return 0;
}
