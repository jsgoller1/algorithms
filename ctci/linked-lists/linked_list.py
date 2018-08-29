import random

class node:
    def __init__(self, value=None):
        self.value = value
        self.next_node = None

# Set up nodes in reverse
def set_up(length, randomize=False):
    if length == 0:
        return None
    list_length = 1
    prev = None
    while(list_length < length):
        if randomize:
            current = node(random.randint(1,100))
        else:
            current = node(list_length)
        current.next_node = prev
        list_length += 1
        prev = current
    return current

def traverse(list_head):
    try:
        assert(isinstance(list_head, node))
    except AssertionError:
        return None
    current = list_head
    print_array = []
    while(current != None):
        print_array.append(current.value)
        current = current.next_node
    return print_array

if __name__ == '__main__':
    print traverse(set_up(20, True))
