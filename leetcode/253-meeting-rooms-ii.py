"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
--------------------------------------------
In: List[Interval]
Out: Int
No constraints
- Any bounds on the times? Can t = 100?

Edge cases:
  - LOTS of meetings
  - No meetings
  - Every meeting overlaps
  - No meetings overlap

- Skiena has a problem similar to this in ADM about how to schedule movie stars
to maximize money, but it might not actually be that similar
- Yeah don't think so, this is an overlapping intervals problem.
- Brute force: test every meeting against every other meeting, determine if an overlap occurs; if so, increment the number of meeting rooms. O(n^2)
- Once we know what time a meeting occurs, we should not need to re-compare to ask "is a meeting occurring at this time"

- What if we sort every intererval by start time and then go through each one, merging overlaps and counting each merge?
  - fails; consider a pattern like [0,2], [1,3], [2,4], [3,5]; would wind up merging them all but only two required

- What if we try a simulation:
  - keep a list times
    - every start and end in sorted order
  - keep two dicts:
    - starting is every interval.start
    - ending is every interval.end
  - keep two ints: available and occupied
    - initialize both to zero

  - Go through every time in times
      - if time in ending:
      - occupied -= ending[time]
      - available += ending[time]
    - if time in starting:
      - occupied += starting[time]
      - set available to max(available -= starting[time], 0)

  return available

- Algorithm is O(nlogn):
  - sorting times takes nlogn time
  - getting starts and ends takes n time
  - simulation takes n time, during which we do many constant operations

- What if multiple meetings start or end at the same time?
  - Use dicts for starts and ends instead, add or subtract those
"""
import collections

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        times = set()
        starting = collections.defaultdict(int)
        ending = collections.defaultdict(int)
        for interval in intervals:
          times.add(interval.start)
          times.add(interval.end)
          starting[interval.start] += 1
          ending[interval.end] += 1

        times = sorted(list(times))
        available = 0
        occupied = 0
        for time in times:
          if time in ending:
            occupied -= ending[time]
            available += ending[time]
          if time in starting:
            occupied += starting[time]
            available = max(available - starting[time], 0)
        return available

if __name__ == '__main__':
  s = Solution()
  assert s.minMeetingRooms([Interval(0, 30), Interval(5, 10), Interval(15, 20)]) == 2
  assert s.minMeetingRooms([Interval(7,10),Interval(2,4)]) == 1
