"""
- We can accomplish this in log(n) time, probably
- If the array were sorted, we could just return arr[0]
- In this case, we need to discover where the original arr[0] is; once this
partition is discovered, we can return it. Call the current index of the old
arr[0] the pivot point

For [4,5,6,7,0,1,2], arr[l] > arr[r] (opposite a normal binary search)
if the midpoint is greater than r, then the pivot will be to the right
  set new l to midpoint
if the midpoint is less than r, the pivot is to the left
  set new r to midpoint

[4,5,6,7,0,1,2]
 l     m     r
       l   m r
       l m r
       l r


[6 7 0 1 2 4 5]
 l     m     r
 l m   r
   l m r
   l r

Above works for nonduplicate arrays, but does it work if duplicates occur? Should.

[4 5 6 7 7 7 0 1 2]
 l       m       r
         l   m   r
         l m r
           l r

[5 6 7 7 7 0 1 2 4]

[0 0 0 0 0 0 0 0 0]

If l and r are equal, we have a problem; this case or
a variant will break our code.
[7,0,7,7,7,7,7,7]
 l             r
if we set l to mid when l and r are equal, we miss the min.
if we set it to r, then the reversed version of this case will cause a miss.
however, if l and r are equal, we can return the min of two recursive cases;
do min(find(l,m),find(m,r))

I _think_ this might devolve to linear time, but might not.
"""


class Solution:
    def recursiveFind(self, nums, l, r, spaces=0):
        while (l < r - 1):
            m = (l + r) // 2
            if nums[l] == nums[r]:
                return min(self.recursiveFind(nums, l, m, spaces + 2), self.recursiveFind(nums, m, r, spaces + 2))
            elif nums[m] > nums[r]:
                l = m
            else:
                r = m
        return min(nums[l], nums[r])

    def findMin(self, nums):
        if not nums:
            return -1
        return self.recursiveFind(nums, 0, len(nums)-1)


s = Solution()
#assert s.findMin([4, 5, 6, 7, 0, 1, 2]) == 0
#assert s.findMin([6, 7, 0, 1, 2, 4, 5]) == 0
#assert s.findMin([5, 6, 7, 7, 7, 0, 1, 2, 4]) == 0
assert s.findMin([4, 5, 6, 7, 7, 7, 0, 1, 2]) == 0
#assert s.findMin([0, 0, 0, 0, 0, 0, 0, 0, 0]) == 0
#assert s.findMin([7, 7, 7, 0, 7, 7, 7, 7]) == 0
