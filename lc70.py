class Solution(object):
    def climbStairs(self, n):
        if n == 0 or n == 1:
            return 1
        dp = [1, 1] + [0 for _ in xrange(n-1)]
        for i in xrange(1,n):
            dp[i+1] = dp[i] + dp[i-1]
        return dp[n]
