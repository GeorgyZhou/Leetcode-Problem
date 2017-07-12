class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        l = len(s)
        dp = [1 for _ in range(l)]
        dp[0] = 9 if s[0] == '*' else 1
        for i in range(1, l):
            if s[i] == '*':
                if s[i-1] == '*':
                    dp[i] = 2 * 9 * dp[i-2] + dp[i-1] * 9
                    continue
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] =  9 * dp[i-2] + dp[i-1] * 9
                    continue
                dp[i] = 9 * dp[i-1]
            else:
                if s[i-1] == '*':
                    dp[i] = 2 * dp[i-2] + dp[i-1]
                    continue
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-1] + dp[i-2]
                    continue
                dp[i] = dp[i-1]
        return dp[-1]
                