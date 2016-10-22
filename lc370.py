class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        updated = [None for i in xrange(length)]
        for i in xrange(len(updates)):
            start, end, inc = updates[i]
            updated[start] = inc if updated[start] is None else updated[start] + inc
            if end+1 < length:
                updated[end+1] = -inc if updated[end+1] is None else updated[end+1] - inc
        amount = 0
        for i in xrange(length):
            if updated[i] is None:
                updated[i] = amount
            else:
                amount += updated[i]
                updated[i]= amount
        return updated
            