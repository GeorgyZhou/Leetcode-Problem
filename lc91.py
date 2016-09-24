class Solution(object):
    def numDecodings(self, s):
        n = len(s)
        if n == 0:
            return 0
        if s[0] == '0':
            return 0
        if n == 1:
            return 1
        dp = [1, 1] + [0 for _ in xrange(n-1)]
        for i in xrange(1, n):
            if s[i-1] == '1':
                dp[i+1] = dp[i-1] if s[i] == '0' else dp[i] + dp[i-1]
            elif s[i-1] == '2' and '0' <= s[i] <= '6':
                dp[i+1] = dp[i] + dp[i-1] if s[i] != '0' else dp[i-1]
            elif s[i] != '0':
                dp[i+1] = dp[i]
            else:
                return 0
        return dp[n]
