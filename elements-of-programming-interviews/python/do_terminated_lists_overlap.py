import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

# if lists are same length and overlap, they overlap at the same place
# so shorten one if necessary, then compare node-by-node.


def get_list_len(head: ListNode):
    size = 0
    while head:
        size += 1
        head = head.next
    return size


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_len = get_list_len(l0)
    l1_len = get_list_len(l1)
    while l0_len > l1_len:
        l0 = l0.next
        l0_len -= 1
    while l0_len < l1_len:
        l1 = l1.next
        l1_len -= 1

    while l0 is not l1:
        l0 = l0.next
        l1 = l1.next

    return l0 if l0 is l1 and l0 is not None else None


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
