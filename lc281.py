class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = []
        self.index = 0
        i = 0
        while i < len(v1) or i < len(v2):
            if i < len(v1):
                self.v.append(v1[i])
            if i < len(v2):
                self.v.append(v2[i])
            i += 1

    def next(self):
        """
        :rtype: int
        """
        ret = self.v[self.index]
        self.index += 1
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.v) >= self.index + 1


        # Your ZigzagIterator object will be instantiated and called as such:
        # i, v = ZigzagIterator(v1, v2), []
        # while i.hasNext(): v.append(i.next())

s = ZigzagIterator([1,2], [3,4,5,6])
print s