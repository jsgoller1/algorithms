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
- what if we used a list of tuples; our "baskets" are [(type,count), (type,count)];
each time we see a new value:
  - it's an item in one of our baskets, so we increment that basket's count?
- this won't work for [0,1,0,1,0,2,0,2]; we can't make use of any zeros sandwiched
between the 1s.

- Looked at related topics, saw "two pointers"; how can we solve this with two pointers?
- I think the two pointers would point at the subarray boundaries
- We don't need direct representations of baskets, just keeping track of values at arr indices
- What about this:
  - biggest = 2
  - start = 0, end = 1
  - for each character in the string from arr[1] to arr[len-1], increment end:
    # might change this to comparison for speed
    if len(set(arr[start], arr[end-1], arr[end])) < 3:
      continue
    else:
      - biggest = max(biggest, len(arr[start:end+1]))
      - walk left from end-1 to the last index where the val == arr[end] or arr[end-1]; set that index to start
  - return len(arr[start:end+1]))
- The approach above is close, but doesn't work for [0, 6, 1, 1, 1, 6, 4, 4, 6] because of the 1s nested between
the 6s; keeping track of "baskets" misses the 1s in between the 6s
- Can we modify the approach so that it works?
- What if the "baskets" are a set created when the indices are created,
and we dump it each time we do the walk-back procedure?
------------------------
- Tried and failed several approaches
"""


class Solution(object):
    def totalFruit(self, tree):
        if len(tree) < 2:
            return len(tree)
        most = 2
        end = 1
        start = 0
        baskets = set([tree[start], tree[end]])
        for i in range(2, len(tree)):
            # print(baskets)
            #print(start, end, i)
            if tree[i] in baskets:
                end = i
                # print("Advanced i to {0} ({1})".format(i, tree[i]))
            elif len(baskets) < 2:
                baskets.add(tree[i])
                end = i
            else:
                # print("Saving {0} (len = {1})".format(
                #    tree[start:end+1], len(tree[start:end+1])))
                most = max(most, len(tree[start:end+1]))
                k = end
                while tree[k-1] == tree[end]:
                    k -= 1
                start = k
                end = i
                baskets = set([tree[start], tree[end]])
        #print(most, len(tree[start:end+1]))
        return max(most, len(tree[start:end+1]))


if __name__ == '__main__':
    s = Solution()
    # Trivial cases
    assert s.totalFruit([]) == 0
    assert s.totalFruit([1]) == 1
    assert s.totalFruit([1, 2]) == 2
    assert s.totalFruit([1, 2, 1]) == 3
    assert s.totalFruit([0, 1, 2, 2]) == 3
    assert s.totalFruit([2, 3, 2, 2]) == 4
    assert s.totalFruit([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]) == 5
    assert s.totalFruit([1, 2, 1, 2, 1, 6, 7, 6, 7, 6, 7, 6, 7]) == 8
    assert s.totalFruit([0, 0, 1, 1]) == 4
    assert s.totalFruit([1, 0, 1, 1]) == 4
    assert s.totalFruit([0, 1, 6, 6, 4, 4, 6]) == 5
    assert s.totalFruit([0, 1, 6, 6, 6, 6, 4, 4, 6]) == 7
    assert s.totalFruit([6, 1, 1, 1, 1, 4, 4]) == 6
    assert s.totalFruit([0, 1, 0, 1, 0, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0])
    assert s.totalFruit([0, 6, 1, 1, 1, 6, 4, 4, 6]) == 5
