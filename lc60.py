class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        if n == 0:
            return "0"
        if n == 1 and k == 1:
            return "1"
        combine = [str(i) for i in xrange(1, n+1)]
        ret = []
        tmp = self.fact(n - 1)
        while len(combine) > 0:
            if k / tmp == len(combine) and k % tmp == 0:
                ret.extend(reversed(combine))
                return ''.join(ret)
            elif k == 1:
                ret.extend(combine)
                return ''.join(ret)
            elif k % tmp == 0:
                ret.append(combine[(k-1)/tmp])
                del combine[(k-1)/tmp]
                ret.extend(reversed(combine))
                return ''.join(ret)
            else:
                ret.append(combine[(k-1)/tmp])
                del combine[(k-1)/tmp]
                k = k % tmp
                tmp /= len(combine)
        return ''.join(ret)
            
        
    
    def fact(self, n):
        if n <= 1:
            return n
        ret = 1;
        for i in xrange(1, n+1):
            ret *= i
        return ret