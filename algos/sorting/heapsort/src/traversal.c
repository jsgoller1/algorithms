#include "heapsort.h"

// Given an index, get the parent's index in the pq
ssize_t pq_parent(ssize_t n) {
  if (n == 1) {
    return -1;
  }
  return (ssize_t)(n / 2);
}

// Given an index n, get its left child in the pq
ssize_t pq_young_child(ssize_t n) { return 2 * n; }
