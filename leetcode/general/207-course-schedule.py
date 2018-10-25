"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have
to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it
possible for you to finish all courses?

Example 1:
Input: 2, [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:
- The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented (link on LC).
- You may assume that there are no duplicate edges in the input prerequisites.

Input: int, number of courses
       list of lists, dependencies
Output: bool; can we finish all courses?

Constraints:
  - No duplicate edges

------------------------------------------------------------------------
Understand

I was curious about topological sorting and specifically looked for LeetCode
questions taggged with it, so I know that this question is related to it.

- A topologically sorted graph is an ordering of a graph's nodes where for every
pair of nodes X and Y with edge XY in between them, X comes before Y in the ordering.
- Said differently, a graph can only be topologically sorted if it contains no directed cycles -
you can start at a node and follow all paths from it without coming back to it.

For this particular question, we need to know if it's possible for us to order the courses
such that we can take all of them; is there any set of dependencies that would make it impossible
to start with a single class and eventually achieve them all?

Example: if you have to to take algorithms before operating systems and networking, networking before
operating systems, and programming before algorithms, you could take the classes in the order of programming,
algorithms, networking, operating systems. However, if with the same courses you had an additional constraint
where you had take algorithms before you took programming, you could not take all the classes as programming
and algorithms require each other.
----------------------
Plan

We can determine if a topological ordering exists by visiting each node in the graph at least once
and collecting its children. Once we know all the children of all the nodes in the graph, we remove
every node that has no children until either every node has children (a cycle exists) or no nodes remain
(no cycle).
------------------------------
Review

Re-evaluating, it occurred to me that you cannot merely keep track of visited nodes;
the question is not "are we visiting the same node twice" but "does a directed cycle exist"?
A cycle exists in an undirected graph if you reach the same node twice, but you can have a diamond
shaped directed graph (A->B,C, B->D, C->D) where you reach the same node twice.
"""


class Solution:
    def removeChildlessNode(self, childlessNode, children):
        for parent in children.keys():
            if childlessNode in children[parent]:
                children[parent].remove(childlessNode)
        del(children[childlessNode])

    def getChildren(self, numCourses, prerequisites):
        children = {i: [] for i in range(numCourses)}
        for prereq in prerequisites:
            children[prereq[1]].append(prereq[0])
        return children

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        children = self.getChildren(numCourses, prerequisites)
        while children:
            noEmpty = True
            for parent in children.keys():
                if children[parent] == []:
                    self.removeChildlessNode(parent, children)
                    noEmpty = False
                    break
            if noEmpty:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) == True
    assert s.canFinish(2, [[1, 0], [0, 1]]) == False
    assert s.canFinish(3, [[0, 1], [0, 2], [1, 2]]) == True
    assert s.canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == True
