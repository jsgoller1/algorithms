# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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



class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.gen = self.generate(nestedList)
        self.peek = self.next() 

    def generate(self, nestedList):
        for item in nestedList:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.generate(item.getList())

    def next(self) -> int:
        ret = self.peek
        try:
            self.peek = next(self.gen)
        except StopIteration:
            self.peek = None 

    def hasNext(self) -> bool:
        return self.peek != None          
