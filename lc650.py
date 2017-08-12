class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        dp = [i for i in range(n+1)]
        dp[1] = 0
        for i in range(4, n+1):
            for j in range(2, i/2 + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i / j)
        return dp[n]