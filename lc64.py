class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        import sys
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        dp = [[sys.maxint for _ in xrange(n+1)] for _ in xrange(m+1)]
        dp[1][1] = grid[0][0]
        for i in xrange(1, m+1):
            for j in xrange(2 if i == 1 else 1, n+1):
                dp[i][j] = grid[i-1][j-1] + min(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
        