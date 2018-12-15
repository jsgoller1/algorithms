"""
Given a char array representing tasks CPU need to do. It contains
capital letters A to Z where different letters represent different
tasks. Tasks could be done without original order. Each task could
be done in one interval. For each interval, CPU could finish one task
or just be idle.

However, there is a non-negative cooling interval n that means between
two same tasks, there must be at least n intervals that CPU are doing
different tasks or just be idle.

You need to return the least number of intervals the CPU will take to
finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.

Note:
- The number of tasks is in the range [1, 10000].
- The integer n is in the range [0, 100].
--------------------------------------------------------------------------
In: list[str], int
Out: int

- Given a list of tasks that need to be executed and an interval
that must elapse before the same task is re-executed, how do we order them?
- We don't really need to keep an array of all the tasks; we are probably going
to have to look at the entire array no matter what, so we can probably compress
it to a dictionary that maps the task name to the number of occurrences. O(n)
- Decrementing each task the number of times it occurrs is also O(n)
- If we "tightly interleave" tasks, we ensure that we idle as little as possible:
  - {a:3, b:3, c:3} = abcabcabc
  - The above is ok for n <= 2, but we will need to add idles if n is larger

- Brute force:
  - Count the number of different tasks in a dict
  - Interleave the tasks as tightly as possible:
    - "while dict is nonempty, for each in dict, decrement task count by 1"
  - Then have a "fixer" that goes through and determines if for each
  task in the array, nothing within n of it is the same; if so, insert an idle.
    - This step could devolve to N^2
---------------------------------------------------------------------------------
- Linear approach:
  - Count the number of different tasks in a dict
  - Maintain as "task string" that represents the order; '0' will be idle
  - Iteratively interleave the tasks as tightly as possible;
    - append 1 of each key where count > 0 to string; delete 0s from dict (caution about delete during iteration)
  - If the number of tasks appended to the string was less than 0, zfill the remainder

- Don't actually need the string since we'd just be returning the length of it
"""
import collections


class Solution:
    def leastInterval(self, tasks, n):
        taskCount = collections.defaultdict(int)
        for task in tasks:
            taskCount[task] += 1
        intervals = 0
        while (taskCount):
            remaining = n + 1
            for task in [task for task in taskCount]:
                if taskCount[task] > 0:
                    intervals += 1
                    remaining -= 1
                    taskCount[task] -= 1
                if taskCount[task] == 0:
                    del taskCount[task]
            if taskCount:
                intervals += max(0, remaining)
        return intervals


if __name__ == '__main__':
    s = Solution()
    # AB0AB0AB
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
    # ABABAB
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
    # AB000000000AB000000000AB000000000
    assert s.leastInterval(["A", "A", "A", "B", "B", "B"], 10) == 24
    # AB0A00A00A00A
    assert s.leastInterval(["A", "A", "A", "A", "A", "B"], 2) == 13
