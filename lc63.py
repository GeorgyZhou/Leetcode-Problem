class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        if n == 0:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
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
                elif obstacleGrid[i-2][j-1] == 1 and obstacleGrid[i-1][j-2] == 1:
                    dp[i][j] = 0
                elif obstacleGrid[i-2][j-1] == 1:
                    dp[i][j] = dp[i][j-1]
                elif obstacleGrid[i-1][j-2] == 1:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
        