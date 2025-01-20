import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
The number of cases here is tricky:
- Lists may or may not overlap
- Lists may or may not contain cycles
- If the lists contain the same cycles, they may enter it at different points. 

We can return any node in their overlap, or none if there's no overlap. 

If neither list contains a cycle, simply check the last node of each. Return it on match, else None. 
If one list contains a cycle and the other doesn't, they don't overlap. Return None. 
If both lists contain a cycle, then hold one pointer fixed and move the other one at a time. If the moving one circles back before
meeting the other, no overlap. If they meet, return the point they meet at. 

"""
def get_tc_node(node):
    """
    A "TC" node (terminal/cyclic node) is a node that is 
    either the last node of a non-cyclic list, or a node
    in the cyclic portion of a cyclic list.
    """
    if not (node and node.next):
        return False, node 
    if not node.next.next:
        return False, node.next 

    slow, fast = node.next, node.next.next 
    while slow != fast: 
        for _ in range(2):
            if fast.next:
                fast = fast.next
            else:
                return False, fast
        slow = slow.next 
    return True, fast 

def overlapping_lists(l0: ListNode, l1: ListNode) -> Optional[ListNode]:
    l0_has_cycle, l0_tc_node = get_tc_node(l0)
    l1_has_cycle, l1_tc_node = get_tc_node(l1)
    if not (l0_has_cycle or l1_has_cycle):
        return l0_tc_node if l0_tc_node == l1_tc_node else None 
    if l0_has_cycle != l1_has_cycle:
        return None 
    l0_init_tc = l0_tc_node
    while l0_tc_node != l1_tc_node:
        l0_tc_node = l0_tc_node.next 
        if l0_tc_node == l0_init_tc:
            return None 
    return l0_tc_node    


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


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_lists_overlap.py',
                                       'do_lists_overlap.tsv',
                                       overlapping_lists_wrapper))
