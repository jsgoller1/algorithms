class node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

class stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, value):
        self.top = node(value, self.top)
        self.size += 1

    def pop(self):
        if self.size > 0:
            ret_val = self.top.value
            self.top = self.top.next_node
            self.size -= 1
            return ret_val
        else:
            return None

    def peek(self):
        if self.top != None:
            return self.top.value
        else:
            return None

    def get_size(self):
        return self.size

if __name__ == '__main__':
    stack = stack()
    for i in range(10):
        stack.push(i)
    while stack.peek() != None:
        print stack.pop()
