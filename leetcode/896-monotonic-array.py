"""
Contest 100 problem
---------
In: List of ints
Out: Bool, is montonic

- increasing = true
- decreasing = true
- for i in range(len(arr)):
  - if arr[i] > arr[i+1]:
    increasing = false
  - if arr[i] < arr[i+1]:
    decreasing = false
return decreasing or increasing
"""
class Solution():
  def isMonotonic(self, arr):
    increasing = True
    decreasing = True
    for i in range(len(arr)-1):
      if arr[i] > arr[i+1]:
        increasing = False
      if arr[i] < arr[i+1]:
        decreasing = False
    return decreasing or increasing

if __name__ == '__main__':
  s = Solution()
  assert s.isMonotonic([1,2,2,3]) ==  True
  assert s.isMonotonic([6,5,4,4]) ==  True
  assert s.isMonotonic([1,3,2]) == False
  assert s.isMonotonic([1,2,4,5]) ==  True
  assert s.isMonotonic([1,1,1]) ==  True
