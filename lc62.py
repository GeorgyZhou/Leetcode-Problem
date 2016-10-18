class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 0 or n == 0:
            return 0
        dp = [[None for _ in xrange(n+1)] for _ in xrange(m+1)]
        for i in xrange(m+1):
            dp[i][0] = 0
        for i in xrange(n+1):
            dp[0][i] = 0
        dp[1][1] = 1
        flag = True
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if flag:
                    flag = False
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]