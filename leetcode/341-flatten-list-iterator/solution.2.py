# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

class NestedInteger:
    pass


def flatten(nested, result):
    if nested.isInteger():
        result.append(nested.getInteger())
        return
    for item in nested.getList():
        flatten(item, result)


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._i = 0
        self._flattened = []
        for val in nestedList:
            flatten(val.getList(), self._flattened)

    def next(self) -> int:
        val = self._flattened[self._i]
        self._i += 1

    def hasNext(self) -> bool:
        return self._i < len(self._flattened)


in_list = [[1, 2, 3], 4, [[5], [6], [[7]]]]
actual = []
expected = [1, 2, 3, 4, 5, 6, 7]
flatten(in_list, actual)
assert actual == expected, f"{in_list}: {actual} != {expected}"
