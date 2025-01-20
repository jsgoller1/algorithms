import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Cases:
    - No cycle, no overlap
    - Cycle, no overlap
    - No cycle, overlap
    - Cycle, overlap 

if only one is cyclic:
    return no overlap
if both are cyclic:
    get beginning of cycle for both. Starting at one,
    if it wraps all the way around without reaching the other's beginning
    of cycle, no overlap 
else:
    shorten to equal length, use
    previous method 
"""


def get_list_len(head: ListNode):
    fast = slow = head
    i = 0
    while slow:
        slow = slow.next
        i += 1
        if fast:
            fast = fast.next
        if fast:
            fast = fast.next
        if fast and fast is slow:
            return -1
    return i


def check_noncyclic_overlap(l0, l0_len, l1, l1_len):
    while l0_len > l1_len:
        l0 = l0.next
        l0_len -= 1

    while l1_len > l0_len:
        l1 = l1.next
        l1_len -= 1

    while l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0


def get_cycle_head(head: ListNode):
    slow = fast = head
    while True:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break

    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast


def check_cyclic_overlap(l0, l1):
    l0_cycle_head = get_cycle_head(l0)
    l1_cycle_head = get_cycle_head(l1)
    if l0_cycle_head is l1_cycle_head:
        return l0_cycle_head

    curr = l0_cycle_head.next
    while curr is not l0_cycle_head:
        if curr is l1_cycle_head:
            return curr
        curr = curr.next
    return None


def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    if not l0 or not l1:
        return None
    l0_len = get_list_len(l0)
    l1_len = get_list_len(l1)

    # One's a cycle, the other is not
    if -1 in [l0_len, l1_len] and l0_len != l1_len:
        return None

    # Neither is cyclic
    if l0_len != -1:
        return check_noncyclic_overlap(l0, l0_len, l1, l1_len)
    else:
        return check_cyclic_overlap(l0, l1)


@enable_executor_hook
def overlapping_lists_wrapper(executor, l0, l1, common, cycle0, cycle1):
    if common:
        if not l0:
            l0 = common
        else:
            it = l0
            while it.next:
                it = it.next
            it.next = common

        if not l1:
            l1 = common
        else:
            it = l1
            while it.next:
                it = it.next
            it.next = common

    if cycle0 != -1 and l0:
        last = l0
        while last.next:
            last = last.next
        it = l0
        for _ in range(cycle0):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    if cycle1 != -1 and l1:
        last = l1
        while last.next:
            last = last.next
        it = l1
        for _ in range(cycle1):
            if not it:
                raise RuntimeError('Invalid input data')
            it = it.next
        last.next = it

    common_nodes = set()
    it = common
    while it and id(it) not in common_nodes:
        common_nodes.add(id(it))
        it = it.next

    result = executor.run(functools.partial(overlapping_lists, l0, l1))

    if not (id(result) in common_nodes or (not common_nodes and not result)):
        raise TestFailure('Invalid result')


def print_list(head):
    seen = set()
    while head:
        if id(head) in seen:
            print("cycle detected; quitting.")
            return
        seen.add(id(head))
        print(f"node: {head.data}")
        head = head.next


if __name__ == '__main__':
    """
    head = curr = ListNode(0, None)
    for i in range(1, 10):
        curr.next = ListNode(i, None)
        curr = curr.next
    # curr.next = head.next.next.next
    print(overlapping_lists(head, head.next.next.next.next).data)
    """
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
