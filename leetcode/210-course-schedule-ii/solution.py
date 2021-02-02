from collections import defaultdict
from typing import List


class CycleExistsError(Exception):
    pass


def visit(course, next_courses, visited, ancestors, top_order):
    if course in visited:
        return
    if course in ancestors:
        raise CycleExistsError

    ancestors.add(course)
    for child in next_courses[course]:
        visit(child, next_courses, visited, ancestors, top_order)
    ancestors.remove(course)
    visited.add(course)
    top_order.append(course)


class Solution:
    def findOrder(self, num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        starting_courses = set([i for i in range(num_courses)])
        next_courses = defaultdict(set)
        for course, prereq in prerequisites:
            next_courses[prereq].add(course)
            starting_courses.remove(course) if course in starting_courses else None
        if not starting_courses:
            return []

        top_order = []
        visited = set()
        while starting_courses:
            ancestors = set()
            curr_course = starting_courses.pop()
            try:
                visit(curr_course, next_courses, visited, ancestors, top_order)
            except CycleExistsError:
                return []
        return top_order[::-1] if len(visited) == num_courses else []


s = Solution()
cases = [
    (2, [[1, 0]]),
    (2, [[1, 0], [0, 1]]),
    (3, [[1, 0], [0, 1]]),
    (4, [[1, 0], [2, 1]])

]
for n_courses, prereqs in cases:
    print(s.findOrder(n_courses, prereqs))
