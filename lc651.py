class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0 for _ in range(N+1)]
        for i in range(N+1):
            dp[i] = i
            for j in range(1, i-3):
                dp[i] = max(dp[i], dp[j] * (i - j - 1))
        return dp[N]