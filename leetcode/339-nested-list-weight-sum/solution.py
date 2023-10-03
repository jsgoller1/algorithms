
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0

        def recurse(ni, depth):
            if ni.isInteger():
                nonlocal total
                total += ni.getInteger() * depth
            else:
                for item in ni.getList():
                    recurse(item, depth+1)
        for item in nestedList:
            recurse(item, 1)
        return total
