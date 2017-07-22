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
        mod = 1e9 + 7
        if s[0] == '*':
            dp[0] = 9
        else:
            dp[0] = 0 if s[0] == '0' else 1
        for i in range(1, l):
            if s[i] == '*':
                if s[i-1] == '*':
                    dp[i] = (15 * dp[i-2] + dp[i-1] * 9) % mod
                elif s[i-1] == '1':
                    dp[i] =  (9 * dp[i-2] + dp[i-1] * 9) % mod
                elif s[i-1] == '2':
                    dp[i] = (6 * dp[i-2] + dp[i-1] * 9) % mod
                else:
                    dp[i] = 9 * dp[i-1] % mod
            else:
                if s[i-1] == '*':
                    if s[i] == '0':
                        dp[i] = 2 * dp[i-2] % mod
                    if '1' <= s[i] <= '6':
                        dp[i] = (2 * dp[i-2] + dp[i-1]) % mod
                    if s[i] > '6':
                        dp[i] = (dp[i-2] + dp[i-1]) % mod
                elif s[i-1] == '1':
                    if s[i] == '0':
                        dp[i] = dp[i-2]
                    else:    
                        dp[i] = (dp[i-1] + dp[i-2]) % mod
                elif s[i-1] == '0':
                    if s[i] == '0':
                        return 0
                    else:
                        dp[i] = dp[i-1]
                elif s[i-1] == '2':
                    if s[i] == '0':
                        dp[i] = dp[i-2]
                    if '1' <= s[i] <= '6':
                        dp[i] = (dp[i-1] + dp[i-2]) % mod
                    else:
                        dp[i] = dp[i-1]
                else:
                    if s[i] == '0':
                        return 0
                    else:
                        dp[i] = dp[i-1]
        return int(dp[-1])