class Solution(object):
    def numWays(self, n, k):
        if n == 0:
            return 0
        if n == 1:
            return 
        self.dp = [0][None for _ in xrange(n+1)]
