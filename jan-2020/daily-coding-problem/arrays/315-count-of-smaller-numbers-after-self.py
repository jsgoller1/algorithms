"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Constraints:
    0 <= nums.length <= 10^5 (up to 100,000 numbers)
    -10^4 <= nums[i] <= 10^4 (each number between -10,000 and 10,000)
-------------------------------------------------------------------------------
Possible cases:
  - Every element after is smaller
  - No elements after are smaller
  - Mixed

Brute force:
  Compare every element in the array to every other (n^2) - with up to 100k elements,
  would be 10b steps (10s according to skeina); would prefer to do better.

Is there a way to re-use information?
  Suppose [4,5,1,2,1,3]

"""
