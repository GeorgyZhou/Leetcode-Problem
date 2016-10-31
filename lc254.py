class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        return self.rec(n, 2, [], [])
    
    def rec(self, n, i, comb, last):
        while i * i <= n:
            if n % i == 0:
                comb.append(last +[i, n/i])
                self.rec(n/i, i, comb, last + [i])
            i += 1
        return combgot a