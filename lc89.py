class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 1:
            return [0, 1]
        elif n == 0:
            return [0]
        m = pow(2,n-1)
        ret = self.grayCode(n-1)
        l = len(ret)
        for i in xrange(l-1,-1,-1):
            ret.append(ret[i] + m)
        return ret