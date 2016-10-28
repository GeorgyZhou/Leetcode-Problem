class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        import sys
        l = len(A)
        if l <= 1:
            return 0
        s, last = 0, 0 
        for i in xrange(l):
            s += A[i]
            last += i * A[i]
        ret = last
        for k in xrange(1, l):
            last = last + s - l*A[l-k]
            ret = max(last, ret)
        return ret