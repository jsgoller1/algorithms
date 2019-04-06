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
-----------------------------------------------------------------------------
- Initial approach failed where we had A:5, B:1, C:1, ... F:1. We should nest
the As between the other characters before we use 0s for padding.
- We need something like a priority queue where the priority is determined
based on both how many characters there are to be used and how recently the
character was used.

Another approach - "priority array":
- We could simply modify our array that keeps the most-needed-to-be-used characters
at the front and maintains a timestamp of most recent use; 0 can be at the end
  - this could get most inefficient in the case of 26 different types of tasks
  and an interval of 26; we could wind up looking at 26 different tasks before deciding
  to use an interval; it would be better to use a data structure that immediately
  tells use what to use next
- Max heaps might be useful, but we run into the issue of needing to get the same value after
n intervals and also not being able to reuse it until n intervals have occurred; if we heapify
based on character count, we would wind up trying to do AAAAAAA, which wouldn't work.
- I think the array sorted by character count and maintaining timestamps is probably
the way to go here. We could wind up looking at 26 chars each iteration, but our current
approach runs that risk too.
- Array approach didn't work as stated due to an edge case where we wind up exhausting
characters early and wind up with a single last character that ends up using interval
padding when it should've been used earlier.

Another approach - math:
- If we have A * 10 and N = 2, then we need 28 intervals (A-wait-wait 10 times until
  the last A, as we don't need two trailing waits). This comes out to ((1 + n) * keycount) - n
- If we have A * 10, B*(less than 10), N=2, we still only need 28 intervals - AB0 until B exhausted, then
  A00 until the last A.
- If we have A * 10, B*(10 or less), C*(10 or less), then we still only need 30; we do ABC
  until B and C are exhausted, then A00 til the last A is used.
- We can extend this reasoning to arbitrarily many groups of characters. If we get our most
  frequently occurring task, we can use the calculation above to build the "skeleton".
  We can then start swallowing the other sets into it by replacing zeroes with characters
  until are zeroes are gone. Once we have depleted all zeroes, we are certain that every character
  is at least N apart, so we can just insert the remaining ones at every N intervals.
- Because we don't need an actual schedule, but just how long at is, we can calculate it as such:
  - get our task counter.
  - get the largest (by occurence) task
  - our skeleton is keycount + (n * keycount-1) long; it cannot be any shorter than this.
  - zeroes are calculated from (n * keycount-1)
  - Then for each less-frequently occurring key, we subtract it from the zero count.
  - Once the zero count is exhuasted, we just add the number of remaining characters.
- The math strategy nearly works but doesn't account for cases where multiple characters
have the same count as the maximum. In these cases, we want to append the other max char
to the end instead of trying to replace other zeroes with it. We can achieve this simply
by decrementing it by 1 and adding 1 to intervals, then processing it normally.
  - A:3, B:3, n=4
  - A0000A0000A
  - AB000AB000AB
"""
import collections

class Solution:
    def leastInterval(self, tasks, n):
        taskCounter = collections.defaultdict(int)
        for task in tasks:
          taskCounter[task] += 1
        remaining = sorted([taskCounter[task] for task in taskCounter], reverse=True)
        maxCount = remaining[0]
        intervals = remaining[0] + (n * (remaining[0] - 1))
        waits = (n * (remaining[0] - 1))
        remaining = remaining[1:]

        while (remaining):
          if remaining[0] == maxCount:
            intervals += 1
            remaining[0] -= 1

          if remaining[0] > waits:
            intervals += (remaining[0] - waits)
            waits = 0
          else:
            waits -= remaining[0]
          remaining = remaining[1:]
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
    # Out: ABCDEFGA00A00A00A00A
    # Best: ABCADEFAG0A00A00A
    assert s.leastInterval(
        ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
    massive = ["G","C","A","H","A","G","G","F","G","J","H","C","A","G","E","A","H","E","F","D","B","D","H","H","E","G","F","B","C","G","F","H","J","F","A","C","G","D","I","J","A","G","D","F","B","F","H","I","G","J","G","H","F","E","H","J","C","E","H","F","C","E","F","H","H","I","G","A","G","D","C","B","I","D","B","C","J","I","B","G","C","H","D","I","A","B","A","J","C","E","B","F","B","J","J","D","D","H","I","I","B","A","E","H","J","J","A","J","E","H","G","B","F","C","H","C","B","J","B","A","H","B","D","I","F","A","E","J","H","C","E","G","F","G","B","G","C","G","A","H","E","F","H","F","C","G","B","I","E","B","J","D","B","B","G","C","A","J","B","J","J","F","J","C","A","G","J","E","G","J","C","D","D","A","I","A","J","F","H","J","D","D","D","C","E","D","D","F","B","A","J","D","I","H","B","A","F","E","B","J","A","H","D","E","I","B","H","C","C","C","G","C","B","E","A","G","H","H","A","I","A","B","A","D","A","I","E","C","C","D","A","B","H","D","E","C","A","H","B","I","A","B","E","H","C","B","A","D","H","E","J","B","J","A","B","G","J","J","F","F","H","I","A","H","F","C","H","D","H","C","C","E","I","G","J","H","D","E","I","J","C","C","H","J","C","G","I","E","D","E","H","J","A","H","D","A","B","F","I","F","J","J","H","D","I","C","G","J","C","C","D","B","E","B","E","B","G","B","A","C","F","E","H","B","D","C","H","F","A","I","A","E","J","F","A","E","B","I","G","H","D","B","F","D","B","I","B","E","D","I","D","F","A","E","H","B","I","G","F","D","E","B","E","C","C","C","J","J","C","H","I","B","H","F","H","F","D","J","D","D","H","H","C","D","A","J","D","F","D","G","B","I","F","J","J","C","C","I","F","G","F","C","E","G","E","F","D","A","I","I","H","G","H","H","A","J","D","J","G","F","G","E","E","A","H","B","G","A","J","J","E","I","H","A","G","E","C","D","I","B","E","A","G","A","C","E","B","J","C","B","A","D","J","E","J","I","F","F","C","B","I","H","C","F","B","C","G","D","A","A","B","F","C","D","B","I","I","H","H","J","A","F","J","F","J","F","H","G","F","D","J","G","I","E","B","C","G","I","F","F","J","H","H","G","A","A","J","C","G","F","B","A","A","E","E","A","E","I","G","F","D","B","I","F","A","B","J","F","F","J","B","F","J","F","J","F","I","E","J","H","D","G","G","D","F","G","B","J","F","J","A","J","E","G","H","I","E","G","D","I","B","D","J","A","A","G","A","I","I","A","A","I","I","H","E","C","A","G","I","F","F","C","D","J","J","I","A","A","F","C","J","G","C","C","H","E","A","H","F","B","J","G","I","A","A","H","G","B","E","G","D","I","C","G","J","C","C","I","H","B","D","J","H","B","J","H","B","F","J","E","J","A","G","H","B","E","H","B","F","F","H","E","B","E","G","H","J","G","J","B","H","C","H","A","A","B","E","I","H","B","I","D","J","J","C","D","G","I","J","G","J","D","F","J","E","F","D","E","B","D","B","C","B","B","C","C","I","F","D","E","I","G","G","I","B","H","G","J","A","A","H","I","I","H","A","I","F","C","D","A","C","G","E","G","E","E","H","D","C","G","D","I","A","G","G","D","A","H","H","I","F","E","I","A","D","H","B","B","G","I","C","G","B","I","I","D","F","F","C","C","A","I","E","A","E","J","A","H","C","D","A","C","B","G","H","G","J","G","I","H","B","A","C","H","I","D","D","C","F","G","B","H","E","B","B","H","C","B","G","G","C","F","B","E","J","B","B","I","D","H","D","I","I","A","A","H","G","F","B","J","F","D","E","G","F","A","G","G","D","A","B","B","B","J","A","F","H","H","D","C","J","I","A","H","G","C","J","I","F","J","C","A","E","C","H","J","H","H","F","G","E","A","C","F","J","H","D","G","G","D","D","C","B","H","B","C","E","F","B","D","J","H","J","J","J","A","F","F","D","E","F","C","I","B","H","H","D","E","A","I","A","B","F","G","F","F","I","E","E","G","A","I","D","F","C","H","E","C","G","H","F","F","H","J","H","G","A","E","H","B","G","G","D","D","D","F","I","A","F","F","D","E","H","J","E","D","D","A","J","F","E","E","E","F","I","D","A","F","F","J","E","I","J","D","D","G","A","C","G","G","I","E","G","E","H","E","D","E","J","B","G","I","J","C","H","C","C","A","A","B","C","G","B","D","I","D","E","H","J","J","B","F","E","J","H","H","I","G","B","D"]
    assert s.leastInterval(massive, 1) == 1000