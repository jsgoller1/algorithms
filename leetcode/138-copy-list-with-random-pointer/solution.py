"""
A linked list is given such that each node contains an additional
random pointer which could point to any node in the list or null.

Return a deep copy of the list.

Input: List node, head of given list
Output: List node, deep copy of inputted list
--------------------------------------
Open questions:
  - Will we be given the head each time, or a node in the middle
  of the list? (Probably given the head)
  - Does the deep copy need to have equivalent references? (probably)
  - Can random point at the node itself?

- Null cases:
  - Empty list (None), return None
  - Singleton - next and random are None, return copy of node

- Edge cases:
  - Node points to a future node in the list; we cannot set a reference to a node that doesn't exist yet
  - Node points to a past node; could cause cycles if we tried a recursive approach.

- This problem is equivalent to a graph-copy problem; could we BFS the "graph" and copy using a visited set
to ensure we don't end up at the same node twice?

- One possible solution:
  - Walk the source list via .next, deep copying; create nodes and put them into a dict based on values.
  - Walk the source list again via .next pointers, but at each source node, get its .random and use it
  as a key to the list dict; set target.random to nodes[source.random.val]
    - Similar to the O(1) LRU, we can have a dictionary of nodes that point to each other;
    this allows for constant time lookups while the nodes maintain references
    to each other (that support linear time lookups)
    - We do not need to use the dict approach; we can just fetch each node linearly as we walk the
    list.
"""

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution(object):
    def copyRandomList(self, head):
      if head == None:
        return

      newHead = RandomListNode(head.label)
      newCurr = newHead
      curr = head.next
      nodes = {newHead.label: newHead}

      while curr != None:
        newNode = RandomListNode(curr.label)
        newCurr.next = newNode
        nodes[curr.label] = newNode
        curr = curr.next
        newCurr = newCurr.next

      curr = head
      newCurr = newHead
      while curr != None:
        if curr.random != None:
          newCurr.random = nodes[curr.random.label]
        else:
          newCurr.random = None
        curr = curr.next
        newCurr = newCurr.next

      return newHead

def createList(size):
    if size < 1:
        return None
    head = RandomListNode(1)
    curr = head
    for i in range(2, size):
        newNode = RandomListNode(i)
        curr.next = newNode
        curr = newNode
    return head

def walkList(head):
    path = ""
    while head != None:
        path += "{0}->".format(head.label)
        head = head.next
    print(path)

if __name__ == '__main__':
  s = Solution()
  rll = createList(10)
  walkList(rll)
  newRll = s.copyRandomList(rll)
  walkList(newRll)

