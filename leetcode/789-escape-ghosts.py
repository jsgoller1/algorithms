"""
Statement

You are playing a simplified Pacman game. You start at the point (0, 0),
and your destination is (target[0], target[1]). There are several
ghosts on the map, the i-th ghost starts at (ghosts[i][0], ghosts[i][1]).

Each turn, you and all ghosts simultaneously *may* move
in one of 4 cardinal directions: north, east, west, or
south, going from the previous point to a new point 1
unit of distance away.

You escape if and only if you can reach the target before
any ghost reaches you (for any given moves the ghosts may take.)
If you reach any square (including the target) at the same
time as a ghost, it doesn't count as an escape.

Return True if and only if it is possible to escape.

Example 1:
Input:
ghosts = [[1, 0], [0, 3]]
target = [0, 1]
Output: true
Explanation:
You can directly reach the destination (0, 1) at time 1,
while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

Example 2:
Input:
ghosts = [[1, 0]]
target = [2, 0]
Output: false
Explanation:
You need to reach the destination (2, 0),
but the ghost at (1, 0) lies between you and the destination.

Example 3:
Input:
ghosts = [[2, 0]]
target = [1, 0]
Output: false
Explanation:
The ghost can reach the target at the same time as you.

Note:
- All points have coordinates with absolute value <= 10000.
- The number of ghosts will not exceed 100.

Input: List of lists of ghost coordinates, and a list of two ints
for the target coordinates we are trying to reach
Output: Bool, whether or not we can reach the target
------
Understand / Plan

- This problem boils down to one question: between pacman and all the ghosts, who
is the closest (with no tie) to the exit? If pacman is the closest, return True.
If a ghost is closest or there is a tie, return false
- Since we're on a grid, "closest" is determined by the lowest Manhattan distance
- To determine the answer, start with Pacman's distance. Then for each ghost,
if its distance is equal to or less than Pacman's, return false. Otherwise, return true
----
Execute

See code below
------
Review

Read these LeetCode discussions:
https://leetcode.com/problems/escape-the-ghosts/discuss/116511/Short-with-explanation-python
https://leetcode.com/problems/escape-the-ghosts/discuss/116678/Why-interception-in-the-middle-is-not-a-good-idea-for-ghosts.
"""


def manhattan_distance(A, B):
    """
    Calculate Manhattan distance
    :type A: List[int]
    :type B: List[int]
    """
    if len(A) != len(B):
        raise ValueError

    return sum([abs(i-j) for i, j in zip(A, B)])


class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        pacman_distance = manhattan_distance([0, 0], target)
        for ghost in ghosts:
            if pacman_distance >= manhattan_distance(target, ghost):
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.escapeGhosts([[1, 0], [0, 3]], [0, 1]) == True
    assert s.escapeGhosts([[1, 0]], [2, 0]) == False
    assert s.escapeGhosts([[2, 0]], [1, 0]) == False
