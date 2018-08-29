import random

"""
Basic
find-max or find-min: find a maximum item of a max-heap, or a minimum item of a min-heap, respectively (a.k.a. peek)
insert: adding a new key to the heap (a.k.a., push[3])
extract-max [or extract-min]: returns the node of maximum value from a max heap [or minimum value from a min heap] after removing it from the heap (a.k.a., pop[4])
delete-max [or delete-min]: removing the root node of a max heap [or min heap], respectively
replace: pop root and push a new key. More efficient than pop followed by push, since only need to balance once, not twice, and appropriate for fixed-size heaps.[5]

Creation
create-heap: create an empty heap
heapify: create a heap out of given array of elements
merge (union): joining two heaps to form a valid new heap containing all the elements of both, preserving the original heaps.
meld: joining two heaps to form a valid new heap containing all the elements of both, destroying the original heaps.

Internal
increase-key or decrease-key: updating a key within a max- or min-heap, respectively
delete: delete an arbitrary node (followed by moving last node and sifting to maintain heap)
sift-up: move a node up in the tree, as long as needed; used to restore heap condition after insertion. Called "sift" because node moves up the tree until it reaches the correct level, as in a sieve.
sift-down: move a node down in the tree, similar to sift-up; used to restore heap condition after deletion or replacement.

             1
     2             3
  4      5      6      7
 8  9  10 11  12 13  14 15

can be serialized to

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

Notes:
- Remember that the number of elements at each depth of the heap is equal to 2 ** depth
- The first element of each depth can be found at array[(2**depth)-1]. In the above array, 4
is the first element at depth 2, and it's at array[2**2-1] == array[3].
- This also means the last element of a depth can be found at array[2**(depth+1)-2].
array[2**(3+1)-2] = array[14], which is 15.
"""
class bin_max_heap:
    def __init__(self, heap_type):
        self.data = []
        self.last_index = -1
        if heap_type in ['min','max']
            self.heap_type = heap_type
        else:
            raise TypeError, 'heap_type must be "min" or "max"'

    def find_max():
        pass

    def insert(self, value):
        self.data.append(value)
        self.last_index += 1
        if self.heap_type == 'max':
            sift_up(data.index(self.last_index))
        else:
            sift_down(data.index(self.last_index))


    def extract_max():
        pass

    def delete_max():
        pass

    def replace():
        pass

    def is_empty():
        return len(self.data) == 0

    def display(self):
        depth = 0
        offset = 0
        while ((2**depth)-1) <= self.last_index:
            this_depth = []
            first = ((2**depth)-1)
            if 2**(depth+1)-1 > self.last_index:
                last = self.last_index
            else:
                last = 2**(depth+1)-2
            for each_node in range(first, last+1): # all of the nodes at this depth, compensated for python's range()
                this_depth.append(self.data[each_node])
            print this_depth
            depth += 1

    def sift_up(idx):
        parent_idx, parent = get_parent(idx)
        tmp = 
        if self.data[idx] > parent:
            tmp = self.data[idx]

            self.data[idx] = parent

    def sift_down():
        pass

    def get_parent(self, index):
        if index == 0 or index > self.last_index:
            return None, None
        parent_index = (index - 1) // 2
        return parent_index, self.data[parent_index]

    def get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index > self.last_index:
            return None
        return left_child_index, self.data[left_child_index]

    def get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index > self.last_index:
            return None
        return right_child_index, self.data[right_child_index]

if __name__ == '__main__':
    heap = bin_max_heap()
    for i in range(1, 16):
        heap.insert(i)
    print heap.data
    heap.display()
    print heap.get_parent(14)
    print "idx/value of left child of 7: ", heap.get_left_child(6)
    print "idx/value of right child of 8: ", heap.get_right_child(8)
    print "idx/value of left child of 8: ", heap.get_left_child(8)
