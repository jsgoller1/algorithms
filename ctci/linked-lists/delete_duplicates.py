from linked_list import node, traverse
import random

def delete_duplicates(head):
    seen_values = {}
    my_node = head
    prev = None
    while my_node != None:
        try:
            x = seen_values[my_node.value] # If we don't get a key error here, we've seen the val before, so remove it.
            prev.next_node = my_node.next_node
            my_node = my_node.next_node
        except KeyError:
            seen_values[my_node.value] = True
            prev = my_node
            my_node = my_node.next_node
    return head


if __name__ == "__main__":
    vals = [1,2,3,4,3,5,6,1,7,8,9,3,10,2,11]
    head = node()
    my_node = head
    for each in vals:
        my_node.value = each
        if each != vals[-1]:
            my_node.next_node = node()
            my_node = my_node.next_node
    print("Linked list before deletions:")
    print(traverse(head))
    head = delete_duplicates(head)
    print("Linked list after deletions:")
    print(traverse(head))
