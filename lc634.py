class Solution(object):
    def findDerangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n-1
        moduler = 10**9 + 7
        dp = [0 for _ in range(n)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n, 1):
            dp[i] = i * (dp[i-1] + dp[i-2]) % moduler
        return dp[-1]