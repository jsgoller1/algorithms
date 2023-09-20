class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        visible = []
        tallest = -float('inf')
        i = len(heights)-1
        while i >= 0:
            if heights[i] > tallest:
                visible.append(i)
                tallest = heights[i]
            i -= 1
        return visible[::-1]
