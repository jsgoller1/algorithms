#include <stdio.h>

#define PQ_SIZE 100
#define ITEM_TYPE size_t

typedef struct priority_queue {
  ITEM_TYPE q[PQ_SIZE + 1]; /* body of queue */
  ssize_t n;                /* number of queue elements */
} priority_queue;

// traversal.c
ssize_t pq_parent(ssize_t n);
ssize_t pq_young_child(ssize_t n);

// construction.c
void pq_init(priority_queue *q);
void pq_insert(priority_queue *q, ITEM_TYPE x);
void pq_swap(priority_queue *q, ssize_t child, ssize_t parent);
void bubble_up(priority_queue *q, ssize_t p);
