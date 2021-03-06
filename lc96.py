class Solution(object):
    def numTrees(self, n):
        if n <= 1:
            return 1
        dp = [1, 1] + [0 for _ in xrange(n-1)]
        for i in xrange(2, n+1):
            for j in xrange(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
