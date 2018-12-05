#include <stdio.h>

#include "heapsort.h"

void pq_init(priority_queue *q) { q->n = 0; }

// Insert a node into the pq, bubbling up if necessary
void pq_insert(priority_queue *q, ITEM_TYPE x) {
  if (q->n >= PQ_SIZE) {
    printf("Warning: priority queue overflow insert x=%lu\n", x);
  }
  q->n = (q->n) + 1;
  q->q[q->n] = x;
  bubble_up(q, q->n);
}

// Swap two nodes in the pq
void pq_swap(priority_queue *q, ssize_t i, ssize_t j) {
  ITEM_TYPE temp;
  temp = q->q[i];
  q->q[i] = q->q[j];
  q->q[j] = temp;
}

// recursively exchange a node with its parent
// until the heap property applies
void bubble_up(priority_queue *q, ssize_t p) {
  if (pq_parent(p) == -1) {
    /* at root of heap, no parent */
    return;
  }
  if (q->q[pq_parent(p)] > q->q[p]) {
    pq_swap(q, p, pq_parent(p));
    bubble_up(q, pq_parent(p));
  }
}
