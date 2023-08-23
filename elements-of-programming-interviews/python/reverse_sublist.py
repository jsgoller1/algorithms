from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def reverse_list(start: ListNode, end: ListNode) -> None:
    if start == end:
        return
    prev = None
    curr = start
    while prev != end:
        nextNext = curr.next
        curr.next = prev
        prev = curr
        curr = nextNext


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not start or start == finish:
        return L
    pre_start_node = start_node = end_node = post_end_node = None
    curr = L
    i = 1
    while curr:
        if i == start-1:
            pre_start_node = curr
        elif i == start:
            start_node = curr
        elif i == finish:
            end_node = curr
        elif i == finish+1:
            post_end_node = curr
        i += 1
        curr = curr.next

    reverse_list(start_node, end_node)
    # if there was a pre-start node, it points now to end node
    if pre_start_node:
        pre_start_node.next = end_node
    # if there was a post-end node, the old start node now points to it.
    if post_end_node:
        start_node.next = post_end_node
    return L if pre_start_node else end_node


if __name__ == '__main__':
    """
    start_i = 1
    finish_i = 9
    head = start = finish = end = ListNode(0, None)

    for i in range(1, 10):
        end.next = ListNode(i, None)
        end = end.next
        if i == start_i:
            start = end
        if i == finish_i:
            finish = end
    reverse_sublist(head, start_i, finish_i)

    while (head):
        print(f"Node: {head.data}")
        head = head.next

    """
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
