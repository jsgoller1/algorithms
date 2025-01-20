import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_list_len(node):
    length = 0 
    if not node:
        return length
    while node:
        node = node.next 
        length += 1 
    return length

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    l0_len, l1_len = get_list_len(l0), get_list_len(l1)
    while l0_len != l1_len:
        l0, l1 = (l0.next, l1) if l0_len > l1_len else (l0, l1.next)
        l0_len, l1_len = (l0_len-1, l1_len) if l0_len > l1_len else (l0_len, l1_len-1)
    while l0 != l1:
        l0, l1 = l0.next, l1.next 
    return l0 


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
