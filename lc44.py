class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens, lenp = len(s), len(p)
        dp = [[False] * (lenp + 1) for _ in xrange(lens + 1)]
        dp[0][0] = True
        flag = False
        if s and not p:
            return False
        i = 0
        while i < lenp and p[i] == '*':
            dp[0][i+1] = True
            i += 1
        for i in xrange(lens):
            for j in xrange(lenp):
                if p[j] == '*':
                    dp[i+1][j+1] = dp[i+1][j] or dp[i][j] or dp[i][j+1]
                elif p[j] == '?' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
        return dp[lens][lenp]

solution = Solution()
print solution.isMatch('aa', 'aa')