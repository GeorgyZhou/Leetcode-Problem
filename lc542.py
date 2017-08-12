class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        import sys
        if not matrix or not matrix[0]:
            return matrix
        m, n = len(matrix), len(matrix[0])
        dp = [[sys.maxint for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i-1][j] if i >= 1 else sys.maxint, dp[i][j-1] if j >= 1 else sys.maxint) + 1
                else:
                    dp[i][j] = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if matrix[i][j] == 1:
                    tmp = min(dp[i+1][j] if i < m-1 else sys.maxint, dp[i][j+1] if j < n-1 else sys.maxint) + 1
                    dp[i][j] = min(tmp, dp[i][j])
                else:
                    dp[i][j] = 0
        return dp