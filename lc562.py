class Solution(object):
    def longestLine(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        if not M or not M[0]:
            return 0
        m, n = len(M), len(M[0])
        dp = [[[0, 0, 0, 0] for _ in range(n+1)] for _ in range(m+1)]
        ret = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if M[i-1][j-1] == 1:
                    dp[i][j][1] = dp[i-1][j-1][1] + 1
                    dp[i][j][0] = dp[i][j-1][0] + 1
                    dp[i][j][2] = dp[i-1][j][2] + 1
                    dp[i][j][3] = dp[i-1][j+1][3] + 1 if j < n else 1
                    ret = max(max(dp[i][j]), ret)
        return ret