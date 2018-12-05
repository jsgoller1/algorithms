#include <stdio.h>

#include "heapsort.h"

// Intialize a heap's item counter
void pq_init(priority_queue *q) { q->n = 0; }

// Initialize the heap
void make_heap(priority_queue *q, ITEM_TYPE s[], size_t item_count) {
  pq_init(q);
  for (size_t i = 0; i < item_count; i++) {
    pq_insert(q, s[i]);
  }
}
