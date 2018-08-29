import random

instructions = """

Design a stack that supports the max() operation for the maximum int
stored within it, and throws an error (returns None in this case) if it is
empty. Use minimal additional space beyond storing the elements themselves,
and O(1) time operations. (EPI 8.1)

The tricky part here is handling situations where the stack stores multiple max
values - for instances, what happens if 300 is the max, and then 300 is pushed
4 more times, only for 500 to be pushed 3 times after that, and so on?

We can accomplish optimal performance with the use of an auxiliary stack.
Our main stack will store our actual values, and the aux stack will store lists
in the form of [value, number of occurences]. Every time we push a value
to the main stack, one of three things happens:
1) the value is less than aux_stack.top()[0] and we do nothing.
2) the value is equal to aux_stack.top()[0], and we increment aux_stack.top()[1]
3) the value is greater than aux_stack.top()[0], so we push (value, 1) on
the aux stack

When pop from the main stack, one of two things happens:
1) the popped value is less than aux_stack.top()[0] and we do nothing.
2) the popped value is equal to aux_stack.top()[0], so we decrement
aux_stack.top()[1]. If aux_stack.top()[1] is equal to 0, we pop the top of the
aux stack.
"""

class node:
    def __init__(self, value=None):
        self.value = value
        self.Next = None

class aux_stack:
    def __init__(self):
        self.top = None

    def current_max(self):
        return self.top.value[0]

    def handle_push(self, value):
        if self.top == None:
            new_node = node([value, 1])
            new_node.Next = self.top
            self.top = new_node
        else:
            if self.top.value[0] > value:
                return
            elif self.top.value[0] == value:
                self.top.value[1] += 1
            else: # self.top.value[0] < value
                new_node = node([value, 1])
                new_node.Next = self.top
                self.top = new_node

    def handle_pop(self, value):
        if value < self.top.value[0]:
            return
        else: # value == self.top.value[0]
            self.top.value[1] -= 1
            if self.top.value[1] == 0:
                self.top = self.top.Next

class max_stack:
    def __init__(self):
        self.top = None
        self.aux = aux_stack()

    def push(self, value):
        new_node = node(value)
        new_node.Next = self.top
        self.top = new_node
        self.aux.handle_push(value)

    def pop(self):
        value = self.top.value
        self.top = self.top.Next
        self.aux.handle_pop(value)
        return value

    def peek(self):
        current = self.top
        while current is not None:
            print current.value
            current = current.Next

    def max(self):
        return self.aux.current_max()


#if __name__ == '__main__':
if __name__ == 'max_stack':
    print instructions
    stack = max_stack()
    for number in range(1, 20):
        stack.push(random.randint(0,100))
