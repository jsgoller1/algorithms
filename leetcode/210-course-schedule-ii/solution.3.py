"""
Topological sort via DFS:
    - launch a dfs from every node, with our white/grey/black strategy
    - during our DFS, if a node has no children, we can add it to the top order
    - otherwise, explore each of its children, and then once done, add it to the top ordering. 
"""

from typing import List


class Solution:
    def dfs(self, course, courses, visited, dfs_visited, top_order):
        if course in dfs_visited:
            return False
        if course in visited:
            return True
        dfs_visited.add(course)
        for next_course in courses[course]:
            if not self.dfs(next_course, courses, visited, dfs_visited, top_order):
                return False
        dfs_visited.remove(course)
        visited.add(course)
        top_order.append(course)
        return True

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Reverse map of pre-reqs; taking course k allows you to
        # take all of courses[k]
        visited = set()
        courses = {i: [] for i in range(numCourses)}
        for take_second, take_first in prerequisites:
            courses[take_first].append(take_second)

        top_order = []
        for course in range(numCourses):
            if course in visited:
                continue
            if not self.dfs(course, courses, visited, set(), top_order):
                return []
        return top_order[::-1]


s = Solution()
for case in [
    (2, [[1, 0]], [0, 1]),
    (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 2, 1, 3]),
]:
    numCourses, prereqs, expected = case
    actual = s.findOrder(numCourses, prereqs)
    assert actual == expected, f"{numCourses}, {prereqs}: {actual} != {expected}"
