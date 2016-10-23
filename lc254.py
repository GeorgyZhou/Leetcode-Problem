class Solution(object):
    def __init__(self):
        self.dic = dict()
        self.dic[1] = []
        self.dic[2] = [[2]]
        self.dic[0] = []
    
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        from math import sqrt
        if self.dic.has_key(n):
            return self.dic[n]
        ret = []
        for i in xrange(2, int(sqrt(n))+1):
            if n % i == 0:
                ret.append([i, n/i])
                for com in self.getFactors(n/i):
                    ret.append([i] + com)
        self.dic[n] = ret
        return ret
                    
s = Solution()
print s.getFactors(4)