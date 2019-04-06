"""
Given a time represented in the format "HH:MM", form the next closest
time by reusing the current digits. There is no limit on how many times
a digit can be reused.

You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
and 59 minutes later.

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller
than the input time numerically.
--------------------------------------------------------------------------------
- Problem has more downvotes than upvotes; quickly scanned titles of discussions
to see why people were complaining; saw one title that said BFS and another that
said backtracking (argh, wish I hadn't seen that :( )

- Note that if we remove the ':' symbol, we get an integer and that 24hr times
are monotonically increasing unless they wrap around
- There's 4**4 (256) possible numbers that could come out of any time. Do we need to look at all of them?
  - We need to try finding the least one greater than the current
  - If the above doesn't work, we then need to form the lowest possible valid string
    - can we just take the lowest valid digit and put it in every spot?
  - We can immediately discard any of them where a tens place is greater than 6.
- We can recurse down the string trying to replace each integer with one from the set
  - What direction should our recursion start from? does it matter given it's just 256?
  - how do we know when we've found the right case?
    - try each int in set (lowest to greatest):
      - pick the first one that is greater and valid, go to next place
      - when we're out of string places

For example:
  - 18:57 -> [1,5,7,8], 1857
  - 1851 doesn't work
  - 1855 doesn't work
  - 1857 is the original number
  - 1858 works, add : and return

  - 23:59 -> [2,3,5,9], 2359; correct answer will be 22:22 the next day, but will never come up in this execution
  - 23:5[2-9] don't work
  - 23:[2-9]9 don't work; all less than time
  - 2[2-9]:59 don't work, invalid
  - [2-9]3:59 don't work, invalid

- Edge cases here?
  - make sure that tens places never wind up being greater than 6
  - some are the time itself: 11:11 can only return 11:11
---------------------------------------
After re-examining the problem with some cases on a whiteboard, I came up with the following algorithm:
- go through each character in the string and compare it to the set of available digits:
  - if there is a character in the set greater than the current, set it to the first one we find
    - quit if the resulting time is valid
    - otherwise set the character to the minimum in the set and go to next iteration
"""


class Solution:
    def nextClosestTime(self, time):
        arr = [char for char in time if char != ':']
        digits = sorted(list(set(arr)))
        for i in [3,2,1,0]:
          for digit in digits:
            if arr[i] < digit:
              arr[i] = digit
              if int(arr[0]+arr[1]) <= 23 and int(arr[2]+arr[3]) <= 59:
                return ''.join(arr[:2] + [':'] + arr[2:])
          arr[i] = min(digits)
        return ''.join(arr[:2] + [':'] + arr[2:])


if __name__ == "__main__":
    s = Solution()
    pairs = [
      ("19:34","19:39"),
      ("23:24","23:32"),
      ("23:59","22:22")
    ]
    for pair in pairs:
      print(s.nextClosestTime(pair[0]))
      assert s.nextClosestTime(pair[0]) == pair[1]
