instructions = """
The "merge" of two linked lists A and B is a linked list AB of length (|A| + |B|),
composed of the elements of A and B in some order (in this case, ascending).
For example:
A: 1 -> 3 -> 5 -> 7 -> 9
B: 2 -> 4 -> 6 -> 8
AB: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9

To do this, we go through both A and B, selecting the lesser of the two on each
iteration and appending this to our merged list. If at any point we discover
that one of the two lists has been depleted, then we can either append the remainder
of the other list (shallow copy), or walk through it and append its values (deep
copy).

Time complexity: O(|A|+|B|)
Space complexity: O(|A|+|B|)
"""
import linked_list
import random

def merge_shallow(a_head, b_head):
    if None in [a_head, b_head]:
        return None
    head = current = linked_list.node()
    while(a_head and b_head): # the final node's .next is None
        if a_head.value > b_head.value:
            current.value = a_head.value
            a_head = a_head.next_node
        else: # a_head.value <= b_head.value
            current.value = b_head.value
            b_head = b_head.next_node
        new_node = linked_list.node()
        current.next_node = new_node
        current = new_node

    # One of the lists was empty, so shallow-copy the rest of the other
    non_empty = a_head or b_head
    if non_empty:
        current.value = non_empty.value # resolve dangling value
        current.next_node = non_empty.next_node # append and finish
    return head

if __name__ == '__main__':
    len_ll_a = random.randint(1,20)
    ll_a = linked_list.set_up(len_ll_a)
    len_ll_b = random.randint(1,20)
    ll_b = linked_list.set_up(len_ll_b)
    print "Length of List A: " + str(len_ll_a)
    print "List A: " + str(linked_list.traverse(ll_a))
    print "Length of List B: " + str(len_ll_b)
    print "List B: " + str(linked_list.traverse(ll_b))
    print "AB (merge of A and B): " + str(linked_list.traverse(merge_shallow(ll_a, ll_b)))
