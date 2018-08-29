class node:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

class queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, value):
        self.last = node(value, self.last)
        if self.size == 0:
            # the first node is the first and the last of the queue
            self.first = self.last
        else:
            # if the queue is nonempty, go to the node that was previously the last,
            # and set its previous node to the new node
            self.last.next_node.prev_node = self.last
        self.size += 1

    def dequeue(self):
        if self.size > 0:
            ret_val = self.first.value
            self.first = self.first.prev_node
            self.size -= 1
            return ret_val
        else:
            return None

    def peek(self):
        if self.first != None:
            return self.first.value
        else:
            return None

    def get_size(self):
        return self.size

if __name__ == '__main__':
    queue = queue()
    for i in range(10):
        queue.enqueue(i)
    while queue.peek() != None:
        print queue.dequeue()
