class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return k
        same, dif = k, k*(k-1)
        for i in xrange(2, n):
            same, dif = dif, (same+dif)*(k-1)
        return same+dif
