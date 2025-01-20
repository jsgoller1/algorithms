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
# initialize iterator with nestedList
# res = []
# while iterator.hasNext()
#   append iterator.next() to the end of res
# return res


class NestedIterator:
    def flatten(self, nested_list):
        for item in nested_list:
            if item.isInteger():
                yield item.getInteger()
            else:
                yield from self.flatten(item.getList())

    def __init__(self, nestedList: [NestedInteger]):
        self._gen = self.flatten(nestedList)
        self._ret = next(self._gen)
        self._stopped = False

    def next(self) -> int:
        ret = self._ret
        try:
            self._ret = next(self._gen)
        except StopIteration:
            self._stopped = True
            self._ret = None
        return ret

    def hasNext(self) -> bool:
        return self._stopped


class NestedIteratorExceedsMemory:
    def __init__(self, nestedList: [NestedInteger]):
        self._list = nestedList
        self._idx = 0

    def next(self) -> int:
        nextItem = self._list[self._idx]
        if nextItem.isInteger():
            val = nextItem.getInteger()
            self._idx += 1
            print(f"returning val: {val}")
            return val
        else:
            gen = NestedIterator(nextItem.getList())
            print(f"delving into sublist")
            while gen.hasNext():
                yield gen.next()
            self.idx += 1

    def hasNext(self) -> bool:
        return self._idx < len(self._list)
