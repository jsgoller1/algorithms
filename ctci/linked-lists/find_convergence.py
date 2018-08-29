from linked_list import *
from reverse import reverse
import random

def find_joint(list_a, list_b):
    # Ignore trivial cases
    if None in [list_a, list_b]:
        print "One or more lists are empty, quitting..."
        return

    # The first thing we must do is make sure that the lists are actually joined
    # (whether that means they just contain the same values or literally point to
    # the same memory is left to the interviewer). We do this by walking to the
    # end of each list and confirming they have the same values. We'll also measure
    # the length and save it for later
    end_a = list_a
    len_a = 1
    end_b = list_b
    len_b = 1
    while end_a.next_node != None:
        end_a = end_a.next_node
        len_a += 1
    while end_b.next_node != None:
        end_b = end_b.next_node
        len_b += 1
    if end_b.value != end_a.value:
        print "Lists are not joined!"
        return

    # next_node, we advance the longer list pointer until its list is the same
    # length as the shorter one. Then we can proceed lock step until we hit a
    # duplicate, and that will be our join point.
    if len_b != len_a:
        longer = list_a if len_a > len_b else list_b
        longer_len = len_a if len_a > len_b else len_b
        shorter = list_a if len_a < len_b else list_b
        shorter_len = len_a if len_a < len_b else len_b
        while longer_len > shorter_len:
            longer = longer.next_node
            longer_len -= 1
    else:
        # If the lists are of equal length, just arbitrarily assign a to longer
        # and b to shorter so that we can use the same code
        longer = a
        shorter = b

    # Then proceed lockstep until we hit the same node.
    while(longer != shorter):
        longer = longer.next_node
        shorter = shorter.next_node
    print "Lists join at value: " + str(shorter.value)


if __name__ == "__main__":

    # First, we must create two attached lists.
    # Create two randomly sized lists
    list_a_len = random.randint(1,50)
    list_b_len = random.randint(1,25)

    # List A
    print "List A length: " + str(list_a_len-1)
    list_a = set_up(list_a_len, True)
    print "List A:"
    print(traverse(list_a))

    # List B
    print "List B length: " + str(list_b_len-1)
    list_b = set_up(list_b_len, True)
    print "List B:"
    print(traverse(list_b))

    # Iterate to the end of list_b
    current_b = list_b
    while (current_b.next_node is not None):
        current_b = current_b.next_node

    # Pick a random place in list_a to attach list_b and attach it
    place = random.randint(1, list_a_len)
    current_a = list_a
    for list_node in range(place-1):
        current_a = current_a.next_node
    current_b.next_node = current_a

    # Demo to show the affixing works
    print "List B, affixed to A:"
    print(traverse(list_b))
    print "Prior to running, we know that the lists meet at value: " + str(current_a.value)

    # Find join point
    print("Finding join point...")
    find_joint(list_a, list_b)
