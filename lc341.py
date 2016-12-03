# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
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

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = []
        self.index = -1
        self.rec(nestedList)

    def rec(self, nestedList):
        for ni in nestedList:
            if not ni.isInteger():
                self.rec(ni.getList())
            else:
                self.queue.append(ni.getInteger())
        return

    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.queue[self.index]

    def hasNext(self):
        """
        :rtype: bool
        """
        return False if self.index >= len(self.queue) - 1 else True
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())