class Solution(object):
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        dp = [0] * n
        next_dp = [None] * n
        for i in range(m):
            for j in range(n):
                next_dp[j] = min(dp[max(j - 1, 0)], dp[j], dp[min(j + 1, n - 1)]) + A[i][j]
            for j in range(n):
                dp[j] = next_dp[j]
        return min(dp)
