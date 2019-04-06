"""
Constraints:
  - 0 <= N <= 10 ^ 4; up to 10k cars
  - 0 < target <= 10 ^ 6; up to 1m miles to travel
  - 0 < speed[i] <= 10 ^ 6; cars can go up to 1m mph
  - 0 <= position[i] < target; cars always less than target miles away
  - All initial positions are different.

In: target distance, position array for N cars, speeds of those N cars
Out: How many fleets of cars arrive at destination?

- Distance between cars is irrelevant; if one catches up to another, they become a fleet and arrive simultaenously
- Cars start at different places, going different speeds
- Is this an overalpping intervals problem?
  - Sort cars by position; say once sorted, position[0] closest to target, position[n-1] farthest
  - go through array (maybe use stack for this?) merging cars if they are faster than the car in front of them
  - return number of non-merged car groups remaining
  - is it possible for a car to reach target going slower than a car behind it?
    - what if it starts very close to target?
    - yes
- Brute force approach here is to do an hour-by-hour tick to see if cars merge; can we use math to avoid it? O(n^2)
- Can we answer "would I catch you" in O(c) time?
  - comparing target, sortedPos[i], sortedPos[i+1];
    - if distance/sortedPos[i].speed < (sortedPos[i].distance - sortedPos[i+1].distance)/sortedPos[i+1].speed-sortedPos[i].speed
    we won't catch;
    - Example: target is 50; if car A is at pos 10 going 5mph and car B is at pos 5 going 8 mph, car A reaches target in 5 hours.
      But (10-5)/(8-5) == 5 / 3 == 1.5ish, so car B catches car A after 1.5 h, and they merge
        - if car A is faster than car B, they will not merge.


-----------------------------------------------
- Created array of (pos/speed) pairs sorted low to hi by position (nlogn; do we need to sort / can we do this faster?)
  - Sorting 10k tuples is ok
- For cars A and B in sorted positions:
  - if car A is driving slower than car B, and per calc above car B catches car A before A gets to target, delete A from
  sorted array
    - can't delete during iteration; use while + counters
- return len of sorted array
"""


class Solution(object):
    def timeToTarget(self, target, car):
        return (target-car[0])/car[1]

    def timeToCatch(self, carA, carB):
        if carB[1] <= carA[1]:
            return float('inf')
        else:
            return (carA[0]-carB[0])/(carB[1]-carA[1])

    def carFleet(self, target, position, speed):
        sortedPos = sorted([(pos, mph) for pos, mph in zip(
            position, speed)], key=lambda tup: tup[0], reverse=True)
        print(target, sortedPos)
        carI = 0
        while carI < len(sortedPos) - 1:
            #print(carI, self.timeToCatch(sortedPos[carI], sortedPos[carI + 1]),  self.timeToTarget(target, sortedPos[carI]))
            #print(sortedPos, carI)
            if self.timeToCatch(sortedPos[carI], sortedPos[carI + 1]) <= self.timeToTarget(target, sortedPos[carI]):
                sortedPos.pop(carI+1)
            else:
                carI += 1
        print(sortedPos)
        print("=="*10)
        return len(sortedPos)


if __name__ == '__main__':
    s = Solution()
    assert s.carFleet(target=12, position=[
                      10, 8, 0, 5, 3], speed=[2, 4, 1, 1, 3]) == 3
    assert s.carFleet(target=100, position=[9, 8, 7, 6, 5, 4, 3, 2, 1], speed=[
                      9, 8, 7, 6, 5, 4, 3, 2, 1]) == 9
    assert s.carFleet(target=100, position=[9, 8, 7, 6, 5, 4, 3, 2, 1], speed=[
                      1, 2, 3, 4, 5, 6, 7, 8, 9]) == 1
    assert s.carFleet(target=10, position=[6, 8], speed=[3, 2]) == 2
    assert s.carFleet(target=13, position=[
                      10, 2, 5, 7, 4, 6, 11], speed=[7, 5, 10, 5, 9, 4, 1]) == 2
