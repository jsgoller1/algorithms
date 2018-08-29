import linked_list
import random

def reverse(head, info=True):
    if not isinstance(head, linked_list.node):
        return False
    prev = None
    while(head != None):
        following = head.next_node
        head.next_node = prev
        prev = head
        head = following
    return prev

if __name__ == '__main__':
    myList = linked_list.set_up(random.randint(1,20), True)
    print linked_list.traverse(myList)
    print linked_list.traverse(reverse(myList))
