import math
import collections

"""
https://leetcode.com/problems/perfect-squares/description/
----
Understand

This program will take an int n, and return an output m, where m is the least number of perfect squares.

Question 1: Is this a graph search problem, aside from the fact that it is homework from the graph search class?
Yes - "least number of perfect squares" feels like it is asking "given a starting number 0, what is the shortest
way we can get to n by adding particular types of numbers", and that feels like a shortest path problem. Shortest
path can be achieved with graph search, specifically with BFS.

We can get perfect square numbers simply by taking ints and squaring them.

"What are my nodes and edges representing?"
1. Nodes are sums of integers, edges are "add a specific integer to it"; the root is 0. The only problem with this
approach is that each node has an infinite number of children!
2. Nodes are sums of integers, edges are "subtract a specific integer from it"; the root is n. This is
a better approach, because we can then only work with integers smaller than it, so we don't need to have
an infinite number of children per node.
We will use this approach.

"How am I representing my nodes and edges?"
The nodes will be the integers themselves,
and we can represent distances from the root with a lookup table; since we
are BFSing, the first time we see a value will be the shortest path to it.

----
Plan

- Given n, find its square root.
- Generate a list of all perfect squares less than n, called psquares
- Instantiate a queue and a map called distances; map n to 0.
- Begin BFS; while n > 0
    - For each_number in psquares:
    - if n - each_number > 0 and we haven't seen it before, map it to map[n]+1 and enqueue each_number
        - We don't need to re-test or remap values we've seen before; since this is BFS,
          if we've seen them before, the shortest path to them is the one we've already seen.
    - If n - each_number == 0, return map[each_number] + 1
    - if n - each_number < 0, ignore it.
----
Execute

See below
----
Review

I made two mistakes in my initial approach - firstly, I was re-mapping values we've already seen to longer distances
when we encountered them a second time. Secondly, I was re-adding them to the queue. If we have already seen 33 and know it's
2 squares away from n, we don't need to start another BFS from it, or add a distance that's 4 away from n.
"""


class Solution:
    def numSquares(self, n):
        if 0 <= n <= 2:
            return n

        # Generate perfect squares
        psquares = []
        base = 1
        while base**2 <= n:
            psquares.append(base**2)
            base += 1

        q = collections.deque([n])
        sum_lens = {n: 0}
        while q:
            n = q.popleft()
            for psquare in psquares:
                if n - psquare > 0:
                    # don't increase distance for values we've seen before.
                    if n - psquare not in sum_lens:
                        sum_lens[n - psquare] = sum_lens[n] + 1
                        q.append(n - psquare)
                elif n - psquare == 0:
                    return sum_lens[n] + 1


if __name__ == '__main__':
    s = Solution()
    assert s.numSquares(12) == 3
