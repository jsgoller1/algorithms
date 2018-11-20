"""
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

- Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
- Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you
must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:
Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Example 2:
Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Example 3:
Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:
Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.
--------------------------
In: List[int]
Out: Int

- We given up to n types of trees where len(trees) = n,
we have to "maximize the amount of fruit picked" by picking fruit only from the two most frequent
types of trees.
- We cannot go back and pick fruit from a previous tree; if we first pick at tree[2], any fruit
before it is forfeit.

- This problem feels like it's the same as Top K Most Frequent Elements, except k = 2. Is it?
  - Yes; what we have to do is pick a starting point, then begin our collect->move->collect->move
  process until the end. We cannot skip trees once we start picking fruits.
  - Also, once we have collected two types of fruits, if we encounter a third type, we must halt since
  we can't harvest it.
  - So really this problem is a longest subarray problem, except that the subarray should consist
  of only two different chars.
  - We could probably solve this with dynamic programming.
----------------------------------------------------------------------------
- linear time dp approach:
- establish a cache mapping subarray lengths to tuples of indices
- base cases are array of len 3 or less
  - len 0-2: Return len of array; quit
  - len 3: keep track of indicies; if arr[0] == arr[1] or arr[1] == arr[2], set indices
  as 0,2. Otherwise set them as 1,2
  - len n >= 4: get the indicies for len=n-1. Does arr[n-1] (current element) == arr[n-2] (previous element) or arr[n-3]?
    - Yes: set cache[n] to the same indicies as cache[n-1], but including the current element.
    - No: set cache[n] to (n-1,n)
- at the end, return the maximum subarray size from the cache

constant space, linear time dp approach:
  start with greatest = curr = 2
  for each element starting at 2 and ending at n:
    if arr[each] == arr[each-1] or arr[each] == arr[each-2]:
      curr += 1
    else:
      greatest = max(curr, greatest)
      curr = 2
  return greatest

- cases:
  Trivial: [], [1], [1,2]
  Simple: [1,2,2], [2,2,1]
  Single nontrivial subarray: [1,2,3,4,5,4,5,4,5,4,5,6,7]
  Multiple nontrivial subarrays: [1,2,1,2,1,6,7,6,7,6,7,6,7]

pseudo(arr):
------------------------
- first approach didn't work for all cases; ran into some edge cases like [0,0,0,0] for how we determine baskets
- if we use a set as the basket, we can handle cases like the above
- quit if there are less than 2 trees
- first, establish the baskets based on the first two items (i.e. as as set; it will either have one or two items); set curr to 2
- for each item from 2 to n:
  is the item in the basket?
    yes: increment curr
    no:
      are there two items in the basket already?
        yes: most = max(curr, most), basket = set(tree[i], tree[i-1])
        no: increment curr, add tree[i] to basket
- then return max(curr, most)

- above doesn't work in [0, 1, 6, 6, 6, 6, 4, 4, 6]
- what if we used a list where list[0] is the basket item seen less recently and list[1] is
seen more recently? Then we evict the last recently seen one?
  - would we need to keep counts of how many of each we've seen?
"""

class Solution(object):
    def totalFruit(self, tree):
        if len(tree) < 2:
          return len(tree)

        baskets = set(tree[:2])
        curr = most = 2
        for i in range(2,len(tree)):
          if tree[i] in baskets:
            curr +=1
          else:
            if len(baskets) == 1:
              baskets.add(tree[i])
              curr+=1
            else:
              most = max(curr,most)
              baskets = set([tree[i], tree[i-1]])
              curr = 2

        return max(curr, most)

if __name__ == '__main__':
  s = Solution()
  assert s.totalFruit([]) == 0
  assert s.totalFruit([1]) == 1
  assert s.totalFruit([1,2]) == 2
  assert s.totalFruit([1,2,1]) == 3
  assert s.totalFruit([0,1,2,2]) == 3
  assert s.totalFruit([2,3,2,2]) == 4
  assert s.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) == 5
  assert s.totalFruit([1,2,1,2,1,6,7,6,7,6,7,6,7]) == 8
  assert s.totalFruit([0,0,1,1]) == 4
  assert s.totalFruit([1,0,1,1]) == 4
  assert s.totalFruit([0, 1, 6, 6, 4, 4, 6]) == 5
  assert s.totalFruit([0, 1, 6, 6, 6, 6, 4, 4, 6]) == 7
  assert s.totalFruit([0, 6, 1, 1, 1, 6, 4, 4, 6]) == 5
