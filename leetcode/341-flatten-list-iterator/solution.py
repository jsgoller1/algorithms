"""
Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].
------------------------------------------------------------------------
- Two possible strategies:
  - Lazy: we could try evaluating the input list as the caller requests .next()
    on our nested iterator; this would be more memory efficient and "correct"
    but harder to implement. Not sure how we'd store the "current" state.
  - Pre-loading: as soon as the class is called, read through the entire nested
    list and append values to the flattened array; we either need to use a stack
    or recursion so we can move back up out of nesting. Could TLE depending on
    imposed limits.
  - I think the pre-loading + recursion strategy is probably optimal here. We
    might be able to create a generator via `yield` as a middle ground.

"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):
    def extractor(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                self.items.append(item.getInteger())
            else:
                self.extractor(item.getList())

    def __init__(self, nestedList):
        self.items = []
        self.extractor(nestedList)
        self.index = 0

    def next(self):
        if self.hasNext():
            val = self.items[self.index]
            self.index += 1
            return val

    def hasNext(self):
        return self.index < len(self.items)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
