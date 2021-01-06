"""
While working on LeetCode #743, I discovered that if I popped items from my
priority queue (a list) via heapq.heappop(), my code didn't work if
the items had been added with list.append() instead of heapq.heappush().

Why? both of the heapq() functions maintain the heap invariant; appending
a new element to the heap leaves it invalid if the new element is less than
the min. Similarly, if the new heap[0] isn't the min after a pop(), the invariant
must be restored.
"""
import heapq
import random

if __name__ == '__main__':
    wrong_heap = [random.randint(-100, 100) for i in range(15)]
    correct_heap = []
    for item in wrong_heap:
        heapq.heappush(correct_heap, item)

    other_heap = []
    for item in wrong_heap:
        heapq.heappush(other_heap, item)

    while correct_heap and wrong_heap:
        print("Correct heap: {0}".format(correct_heap))
        print("Correct heap's pop: {0}\n".format(heapq.heappop(correct_heap)))
        print("Other heap: {0}".format(other_heap))
        print("Other heap's pop: {0}\n".format(other_heap.pop(0)))
        print("Wrong heap: {0}".format(wrong_heap))
        print("Wrong heap's pop: {0}".format(heapq.heappop(wrong_heap)))
        print("="*15)
