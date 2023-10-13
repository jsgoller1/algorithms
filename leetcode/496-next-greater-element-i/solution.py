class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []
        for num in nums2:
            next_greater[num] = -1
            if not stack or stack[-1] >= num:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    next_greater[stack[-1]] = num
                    stack.pop()
                stack.append(num)
        return [next_greater[num] for num in nums1]
