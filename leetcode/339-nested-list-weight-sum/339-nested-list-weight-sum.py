class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def recurse(depth, nested):
            total = 0
            for item in nested:
                if item.isInteger():
                    total += (depth * item.getInteger())
                else:
                    total += recurse(depth+1, item.getList())
            return total
        return recurse(1, nestedList)
