from collections import Counter


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_preferences = Counter(students)
        sandwiches = sandwiches[::-1]
        while sandwiches and student_preferences[sandwiches[-1]] != 0:
            student_preferences[sandwiches[-1]] -= 1
            sandwiches.pop()
        return sum(student_preferences.values())
