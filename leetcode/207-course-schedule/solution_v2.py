"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.
Some courses may have prerequisites, for example to take course 0 you have to first take
course 1, which is expressed as a pair: [0, 1] Given the total number of courses and a 
list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should
also have finished course 1. So it is impossible.

Constraints:
    - The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
    - You may assume that there are no duplicate edges in the input prerequisites.
    - 1 <= numCourses <= 10 ^ 5
=================
- Pairs are (course, pre-req)
- This is a classical topological sort problem
    - A topological sorting is an ordering in a DAG where for every directed edge uv from
    vertex u to vertex v, u comes before v in the topological order (there can be many for
    each graph)
    - In this question we need to find a possible way to finish all course - i.e. an ordering where
    we can start with one and eventually complete all of them.
    - Since the pre-reqs form a graph, we are looking for a topological order on the course dependency
    graph.

I know two approaches to topological sorting:

1) Using DFSes; this algorithm runs in O(N) time since it visits each node once,
and uses O(N) space via recursive call stack:
    main()
    Create an empty list that contains the topological sort
    while there are nodes we haven't DFSed yet:
        DFS next node
    return list

    dfs(node)
        if the node has a permanent mark  // visited during a different dfs
            return 
        if the node has a temporary mark  // visited during this DFS, not a dag
            stop everything, no tsort is possible
        
        mark this node with temporary mark
        dfs each child/outgoing node of this node
        remove this node's temporary mark
        mark this node permanently
        add this node to head of main()'s list # Note that this is done on each recursive call

2) Kahn's algorithm
    kahn(graph):
        L = empty list that will contain t sort
        S = set of all nodes with no incoming edges

        while s is nonempty:
            remove a node n from S
            add n to  L
            for each outgoing edge from n to another node m:
                remove the edge
                if m has no other incoming edges:
                    put m into s
        return L if the graph is empty, otherwise throw an error 

Since both of these algorithms work on graphs / input nodes, we'll have to modify them slightly
to leverage them here. We can take the input List[(course,prereq) and use it to construct an
adjacency list. if val is found in adj_list[key], it means an edge exists from key to val. We can
use a default dict mapping courses to sets. Also, we don't need to return a topological order,
just whether one is possible. I'll use the DFS solution:

solution(course_deps):
    adj_list = constructed from input courses with default_dict(set())
    nodes_to_visit = adj_list.keys()
    while nodes_to_visit:
        if not dfs(nodes_to_visit.pop(), set()):
            return False
    return True

dfs(node, current_dfs)
    if node not in adj_list:
        return True
    if node in current_dfs:
        return False
    
    current_dfs.add(node)
    for child in adj_list[node]:
        dfs(child, current_dfs)
    current_dfs.remove(node)
    del adj_list[node]
"""
from typing import List


def dfs(node, adj_list, current_dfs):
    if node not in adj_list:
        return True
    if node in current_dfs:
        return False

    current_dfs.add(node)
    for child in adj_list[node]:
        if not dfs(child, adj_list, current_dfs):
            return False
    current_dfs.remove(node)
    del adj_list[node]
    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = {i: set() for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[prereq].add(course)

        nodes_to_visit = list(adj_list.keys())
        while nodes_to_visit:
            if not dfs(nodes_to_visit.pop(), adj_list, set()):
                return False
        return True


sol = Solution()
cases = [(2, [[1, 0]], True), (2, [[1, 0], [0, 1]], False)]
for num_courses, prereqs, expected in cases:
    actual = sol.canFinish(num_courses, prereqs)
    assert actual == expected, f"{num_courses, prereqs}: {expected} != {actual}"
