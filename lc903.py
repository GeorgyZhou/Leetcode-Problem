class Solution(object):
    def numPermsDISequence(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        mod = 10**9 + 7
        dp = [1] * (n + 1)
        next_dp = [0] * (n + 1)
        for i in range(1, n + 1):
            for j in range(i + 1):
                if S[i - 1] == "D":
                    next_dp[j] = sum(dp[j:i])
                else:
                    next_dp[j] = sum(dp[:j])
            dp, next_dp = next_dp, dp
        return sum(dp) % mod
