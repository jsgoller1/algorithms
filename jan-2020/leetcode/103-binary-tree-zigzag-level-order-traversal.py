"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

return its zigzag level order traversal as:

[
  [3],
  [20,9],
  [15,7]
]

Constraints:
    - None given

Possible cases:
    - Full tree of unbounded depth
    - Single node tree (only root)
    - Mixed tree - some nodes missing
------
Enumerating every node in a tree is doable in O(n) time for n nodes. 

For a normal level order traversal, we use a queue:
    - start with root in queue
    - Append left child, then right
    - pop node, repeat

- We can get level order in reverse by appending right before left. 
- We have to be careful for zigzag - we can't just append alternate left and right. When going left-to-right, we'll get the leftmost children first in the array. 
- Actually, can we just do a level order traveral and right before we append it, we reverse it?
- How do we know when we've finished a level?
    - can't just go by numbers; if the tree isn't full, then we will be missing children 
    - we can queue (node, depth) starting with (root, 0); when we queue children, we add depth+1
    - Then if we determine that this next child's depth differs from the length of our solutions array, we'd append?
-------------------

    3
   / \
  9  20
    /  \
   15   7

queue = deque()
should_reverse = False
solution = [[3], [20,9]]
current_floor = [None, None, 15, 7]

----------------
queue = deque([(root, 0)])
should_reverse = False
solution = []
current_floor = []
while queue is nonempty:
    node, depth = queue.left_pop() 
    if len(solution) != depth:
        solution.append(current_floor.reverse() if should_reverse else current_floor)
        should_revered = not should_reverse
        current_floor = []
    if node:
        current_floor.append(node.value)
        queue.append((node.left, depth+1))
        queue.append((node.right, depth+1))
    else:
        current_floor.append(None)

# make sure to clean up last floor
if current_floor:
    solution.append(current_floor.reverse() if should_reverse else current_floor)

return solution

"""
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque([(root, 0)])
        should_reverse = False
        solution = []
        current_floor = []
        while queue:
            node, depth = queue.popleft()
            if len(solution) != depth:
                solution.append(list(reversed(current_floor)) if should_reverse else current_floor)
                should_reverse = not should_reverse
                current_floor = []
            if node:
                current_floor.append(node.val)
                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        # make sure to clean up last floor
        if current_floor:
            solution.append(list(reversed(current_floor)) if should_reverse else current_floor)

        return solution


if __name__ == '__main__':
    sol = Solution()
    cases = [

    ]
    for root, expected in cases:
        actual = sol.zigzagLevelOrder(in_str, rows)
        assert expected == actual, f"{actual} != {expected}"
