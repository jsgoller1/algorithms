import collections

"""
https://leetcode.com/problems/number-of-islands/description/

This was my interview question for Zenreach! Luckily, I got it right and wound up working there for around a year.
----
Understand

In: list of list of strings, representing a grid
Out: int

This question is a "connected components" question. Given our input, we know how many nodes there are in our graph and can
access each one individually. We must test to see how many unconnected subgraphs exist in our graph, where "unconnected" means
that no path exists from one graph to another.

----
Plan

My first approach:
We can keep a running count of the number of islands we've seen starting with 0. We then
iterate through the array, BFSing at each node we find, changing it to 'X' to indicate
we've already seen it. If we exhaust a BFS and never see an X, increment islands. If
we encounter an X in our BFS, quit. During our BFS, we don't need to look up or left
since it will either take us out of array or show us nodes we've already seen before.

My second approach:
During our BFS, we should "sink" the islands by setting each one to '0' as we BFS, eventually returning True.
We immediately return False if we start on a '0'. This way, we will never accidentally quit too early, nor will
we have to distinguish between nodes we saw _this_ BFS vs ones we saw during a previous one.

----
Execute

See below
----
Review

My first approach didn't work so well, because I would end up enqueuing nodes I had seen before, and
it became hard to tell if they were from my current BFS or a previous one. Because of this, the algorithm would
fail or give incorrect answers.
----
"""


def island_bfs(grid, y, x):
    if grid[y][x] == '0':
        return False

    q = collections.deque([[y, x]])
    while q:
        coords = q.popleft()
        y = coords[0]
        x = coords[1]
        if grid[y][x] == '1':
            grid[y][x] = '0'
            if y > 0:
                q.append([y-1, x])
            if y < (len(grid) - 1):
                q.append([y+1, x])
            if x > 0:
                q.append([y, x-1])
            if x < (len(grid[y]) - 1):
                q.append([y, x+1])

    return True


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islands = 0

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if island_bfs(grid, y, x):
                    islands += 1

        return islands


if __name__ == '__main__':
    s = Solution()
    assert s.numIslands([['1', '1', '1', '1', '0'], ['1', '1', '0', '1', '0'], [
                        '1', '1', '0', '0', '0'], ['0', '0', '0', '0', '0']]) == 1
