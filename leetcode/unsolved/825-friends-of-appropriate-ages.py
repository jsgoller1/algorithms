"""
Person A will NOT friend request person B (B != A) if any of the following conditions are true:
1. age[B] <= 0.5 * age[A] + 7
2. age[A] < age[B]
3. age[B] > 100 && age[A] < 100

How many requests?

Constraints:
1 <= ages.length <= 20000.
1 <= ages[i] <= 120.

- Condition 2 fully covers condition 1; if A is under 100 and B is over 100, age[A] < age[B],
so it doesn't matter
- Problem can be restated as "A request B if B is between ages[A] and (ages[A] // 2) + 7."
So how do we count this quickly?
- If we sort and start with the oldest index and the index of the first that is too young,
the number of elements between them is the number of friend requests the oldest makes. E.g.
3 here:
[54, 57, 58, 58, 60, 100]
     1                5
- If we start at the oldest and find the index of the first age that doesn't meet the
criteria, we can work our way downwards in linear time by keeping track of the "window" of allowed
ages.
- If we sort first, we don't need to increment the window pointer as we move down;
54//2 + 7 is always less than 100//2 + 7

Some cases:
[58, 58, 58, 58, 60, 100] - all allowed, subtract youngest index from oldest
 0                    5
 [50, 51, 52, 53, 54, 100] - none allowed, subtract youngest index from oldest
 0                    5
"""
import collections


class Solution:
    def numFriendRequests(self, ages):
        ageCounts = collections.Counter(ages)
        ages = sorted(set(ages))
        total = 0
        for i in range(len(ages) - 1, -1, -1):
            # all duplicate ages friend request each other
            age = ages[i]
            total += ageCounts[age] * (ageCounts[age] - 1)
            #print(age, total)

            # for each younger one, friend request
            # younger ones up to threshold
            ageSlice = ages[:i]
            for younger in reversed(ageSlice):
                if younger <= (age // 2 + 7):
                    break
                total += ageCounts[younger] * ageCounts[age]
        # print(total)
        return total


if __name__ == '__main__':
    s = Solution()
    assert s.numFriendRequests([16, 16]) == 2
    assert s.numFriendRequests([16, 17, 18]) == 2
    assert s.numFriendRequests([20, 30, 100, 110, 120]) == 3
    assert s.numFriendRequests([8, 24, 69, 85, 85]) == 4
    assert s.numFriendRequests(
        [73, 106, 39, 6, 26, 15, 30, 100, 71, 35, 46, 112, 6, 60, 110]) == 29
