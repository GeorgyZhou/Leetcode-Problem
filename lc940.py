class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        dp = [1]
        showed = {}
        for i, c in enumerate(S):
            dp.append(dp[i] * 2)
            if c in showed:
                dp[-1] -= dp[showed[c]]
            showed[c] = i
        return (dp[-1] - 1) % (10**9 + 7)
